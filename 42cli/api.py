#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json
import importlib
import sys

import click
from halo import Halo

const = importlib.import_module('42cli.const')
util = importlib.import_module('42cli.util')


def apiGetUsers(authInfo):
    username = util.getConfig().username
    path = "https://api.intra.42.fr/v2/users/{}/?".format(username)
    return apiAccess(authInfo, path)


def apiGetProjectsUsers(authInfo, id_):
    path = "https://api.intra.42.fr/v2/projects_users/{}?".format(id_)
    return apiAccess(authInfo, path)


def apiAccess(authInfo, path):
    param = urllib.parse.urlencode(authInfo)
    url = path + param
    spinner = Halo(text=const.MSG_ACCESSING_API, spinner='dots')
    spinner.start()
    try:
        with urllib.request.urlopen(url) as response:
            apiResponse = json.loads(response.read().decode("utf-8"))
    except Exception:
        spinner.fail()
        click.secho(const.MSG_API_ACCESS_ERROR, fg='red')
        sys.exit(1)
    else:
        spinner.succeed()
        return apiResponse
