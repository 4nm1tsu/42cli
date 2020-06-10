#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
from datetime import datetime

authorize = importlib.import_module("fortytwocli.authorize")
api = importlib.import_module("fortytwocli.api")
const = importlib.import_module("fortytwocli.const")


def showStatus():
    authInfo = authorize.getAuthInfo()
    apiResponse = api.apiGetUsers(authInfo)

    # basic information
    print('{}<{}>'.format(apiResponse['login'], apiResponse['email']))
    # evaluation point
    print('Eval points: ' + str(apiResponse['correction_point']))

    # black hole date
    for cursus in apiResponse['cursus_users']:
        if cursus['blackholed_at'] is not None:
            blackHole = datetime.strptime(
                cursus['blackholed_at'],
                '%Y-%m-%dT%H:%M:%S.%fZ'
            )
            limit = blackHole - datetime.now()
            print("{}: {} days left".format(cursus['cursus']['name'],
                                            limit.days))

    # project in progress
    projects = []
    for project in apiResponse['projects_users']:
        if project['status'] == 'in_progress':
            projects.append(project['project']['name'])
    if len(projects) == 0:
        print(const.MSG_NO_PROJECT_IN_PROGRESS)
    for project in projects:
        print(project)

    # optionで管理 -aで全て
    # cursus毎にレベル、スキルなど表示したい!
    # termgraph
    # review予定もここで
