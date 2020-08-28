#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json

from halo import Halo

import fortytwocli.const as const
import fortytwocli.util as util
import fortytwocli.exception as exception


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
        raise exception.ApiAccessError(const.MSG_API_ACCESS_ERROR)
    else:
        spinner.succeed()
        return apiResponse
