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


def openFileToWrite(path, content):
    with open(path, 'wb') as fp:
        pickle.dump(content, fp)


def openFileToRead(path):
    with open(path, 'rb') as fp:
        return pickle.load(fp)


def authorize():
    config = openFileToRead(ROOT_DIR+'/'+const.CONFIG_FILE)
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
    openFileToWrite(
        ROOT_DIR+'/'+const.CACHE_FILE,
        Cache(auth_info, deadline)
    )

    return auth_info


def getAuthInfo():
    # cacheが存在する場合
    if os.path.exists(ROOT_DIR+'/'+const.CACHE_FILE):
        cache = openFileToRead(ROOT_DIR+'/'+const.CACHE_FILE)
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
