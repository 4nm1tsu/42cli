#!/usr/bin/env python
# -*- coding: utf=8 -*-

import urllib.request
import urllib.parse
import json
import importlib

authorize = importlib.import_module("42cli.authorize")


def showUserName():
    auth_info = authorize.getAuthInfo()

    param = urllib.parse.urlencode(auth_info)
    url = "https://api.intra.42.fr/v2/users/{}/?".format('hokada') + param

    try:
        with urllib.request.urlopen(url) as res:
            api_res = json.loads(res.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print('No such user!')
        exit()

    print('login: ' + api_res['login'])
    print('first_name: ' + api_res['first_name'])
    print('last_name: ' + api_res['last_name'])
    print('id: ' + str(api_res['id']))
    print('email: ' + api_res['email'])
