#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json
import importlib
import time
import os
import sys

import click
from halo import Halo

from definitions import ROOT_DIR
const = importlib.import_module('42cli.const')
util = importlib.import_module('42cli.util')


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
        auth_info = json.loads(res.read().decode("utf-8"))
    # cacheに保存
    deadline = time.time() + int(auth_info['expires_in'])
    util.openFileToWrite(
        ROOT_DIR+'/'+const.CACHE_FILE,
        Cache(auth_info, deadline)
    )

    return auth_info


def getAuthInfo():
    # cacheが存在する場合
    if os.path.exists(ROOT_DIR+'/'+const.CACHE_FILE):
        cache = util.getCache()
        # 期限OK
        if cache.deadline > time.time():
            auth_info = cache.auth
        # 期限NG
        else:
            spinner = Halo(text=const.MSG_REQUEST_TOKEN, spinner='dots')
            spinner.start()
            try:
                auth_info = authorize()
            except Exception:
                spinner.fail()
                click.secho(const.MSG_AUTHORIZE_ERROR, fg='red')
                sys.exit(1)
            else:
                spinner.succeed()
    else:
        spinner = Halo(text=const.MSG_REQUEST_TOKEN, spinner='dots')
        spinner.start()
        try:
            auth_info = authorize()
        except Exception:
            spinner.fail()
            click.secho(const.MSG_AUTHORIZE_ERROR, fg='red')
            sys.exit(1)
        else:
            spinner.succeed()

    return auth_info
