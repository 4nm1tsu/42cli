#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import urllib.request
import urllib.parse
import json
import importlib
import time
import os

import click

from definitions import ROOT_DIR
const = importlib.import_module('42cli.const')


class Cache:
    def __init__(self, auth, deadline):
        self.auth = auth
        self.deadline = deadline


def authorize():
    with open(ROOT_DIR+'/'+const.CONFIG_FILE, 'rb') as fp:
        config = pickle.load(fp)
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
    with open(ROOT_DIR+'/'+const.CACHE_FILE, 'wb') as fp:
        pickle.dump(Cache(auth_info, deadline), fp)

    return auth_info


def getAuthInfo():
    # cacheが存在する場合
    if os.path.exists(ROOT_DIR+'/'+const.CACHE_FILE):
        with open(ROOT_DIR+'/'+const.CACHE_FILE, 'rb') as fp:
            cache = pickle.load(fp)
        # 期限OK
        if cache.deadline > time.time():
            auth_info = cache.auth
        # 期限NG
        else:
            click.secho(const.MSG_MAKE_CACHE, fg="green")
            auth_info = authorize()
    else:
        click.secho(const.MSG_MAKE_CACHE, fg="green")
        auth_info = authorize()

    return auth_info
