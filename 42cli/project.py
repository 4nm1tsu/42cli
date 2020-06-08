#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

authorize = importlib.import_module("42cli.authorize")
api = importlib.import_module("42cli.api")


def showUserName():
    auth_info = authorize.getAuthInfo()
    api_res = api.apiGetUsers(auth_info)

    print('login: ' + api_res['login'])
    print('first_name: ' + api_res['first_name'])
    print('last_name: ' + api_res['last_name'])
    print('id: ' + str(api_res['id']))
    print('email: ' + api_res['email'])
