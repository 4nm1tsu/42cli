#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

import inquirer
import git
import click

authorize = importlib.import_module("fortytwocli.authorize")
api = importlib.import_module("fortytwocli.api")
const = importlib.import_module("fortytwocli.const")
exception = importlib.import_module("fortytwocli.exception")


def cloneProject():
    authInfo = authorize.getAuthInfo()
    apiResponse = api.apiGetUsers(authInfo)

    choices = {}
    for project in apiResponse['projects_users']:
        # 'in_progress' or 'finished'
        if project['status'] == 'in_progress':
            choices[project['project']['name']] = project['id']

    if len(choices) == 0:
        click.secho(const.MSG_NO_AVAILABLE_REPO, fg='cyan')
        return
    # lenが1のときに自動で選択することはしない→ユーザへのFeedbackがないので
    else:
        questions = [
            inquirer.List(
                "name",
                message="What project do you want to clone?",
                choices=choices.keys(),
                carousel=True,
            )
        ]

        answer = inquirer.prompt(questions)
        projectName = answer['name']
        id_ = choices[projectName]

    apiResponse = api.apiGetProjectsUsers(authInfo, id_)

    if len(apiResponse['teams']) > 1:
        choices = {}
        for project in apiResponse['teams']:
            choices[project['name']] = project['repo_url']

        questions = [
            inquirer.List(
                "team",
                message="What project do you want to clone?",
                choices=choices.keys(),
                carousel=True,
            )
        ]

        answer = inquirer.prompt(questions)
        url = choices[answer['team']]
    else:
        url = apiResponse['teams'][0]['repo_url']

    try:
        git.Repo.clone_from(url, projectName)
    except Exception:
        raise exception.GitError(const.MSG_GIT_ERROR)
