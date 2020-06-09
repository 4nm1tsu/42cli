#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

authorize = importlib.import_module("42cli.authorize")
api = importlib.import_module("42cli.api")


def showStatus():
    authInfo = authorize.getAuthInfo()
    apiResponse = api.apiGetUsers(authInfo)

    print('login: ' + apiResponse['login'])
    print('email: ' + apiResponse['email'])
    print('Eval points: ' + str(apiResponse['correction_point']))
    # cursus毎にレベル、スキルなど表示したい!
    # termgraph
    for cursus in apiResponse['cursus_users']:
        print(cursus['cursus']['name'], ': ', cursus['blackholed_at'])
