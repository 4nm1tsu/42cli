#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json
import importlib

import click

const = importlib.import_module('42cli.const')
util = importlib.import_module('42cli.util')


def apiGetUsers(auth_info):
    param = urllib.parse.urlencode(auth_info)
    username = util.getConfig().username
    url = "https://api.intra.42.fr/v2/users/{}/?".format(username)\
        + param
    try:
        with urllib.request.urlopen(url) as response:
            api_response = json.loads(response.read().decode("utf-8"))
    except Exception:
        click.secho(const.MSG_API_ACCESS_ERROR, fg='red')
        exit()
    else:
        return api_response
