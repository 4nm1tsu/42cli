#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json
import importlib
import time
import os

from halo import Halo

const = importlib.import_module('fortytwocli.const')
util = importlib.import_module('fortytwocli.util')
exception = importlib.import_module("fortytwocli.exception")


class Cache:
    def __init__(self, auth, deadline):
        self.auth = auth
        self.deadline = deadline


def authorize():
    config = util.getConfig()
    data = {
            "grant_type": "client_credentials",
            "client_id": config.uid,
            "client_secret": config.secret,
            }
    data = urllib.parse.urlencode(data).encode("utf-8")
    token_url = "https://api.intra.42.fr/oauth/token"
    with urllib.request.urlopen(token_url, data=data) as res:
        authInfo = json.loads(res.read().decode("utf-8"))
    # cacheに保存
    deadline = time.time() + int(authInfo['expires_in'])
    util.openFileToWrite(
        const.CACHE_FILE,
        Cache(authInfo, deadline)
    )

    return authInfo


def getAuthInfo():
    # cacheが存在する場合
    if os.path.exists(const.CACHE_FILE):
        cache = util.getCache()
        # 期限OK
        if cache.deadline > time.time():
            authInfo = cache.auth
        # 期限NG
        else:
            spinner = Halo(text=const.MSG_REQUEST_TOKEN, spinner='dots')
            spinner.start()
            try:
                authInfo = authorize()
            except Exception:
                spinner.fail()
                raise exception.AuthorizeError(const.MSG_AUTHORIZE_ERROR)
            else:
                spinner.succeed()
    else:
        spinner = Halo(text=const.MSG_REQUEST_TOKEN, spinner='dots')
        spinner.start()
        try:
            authInfo = authorize()
        except Exception:
            spinner.fail()
            raise exception.AuthorizeError(const.MSG_AUTHORIZE_ERROR)
        else:
            spinner.succeed()

    return authInfo
