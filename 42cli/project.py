#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
from pprint import pprint

authorize = importlib.import_module("42cli.authorize")
api = importlib.import_module("42cli.api")


def showRawResponse():
    auth_info = authorize.getAuthInfo()
    api_res = api.apiGetUsers(auth_info)

    pprint(api_res)
