#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import sys

import inquirer
import git
import click

authorize = importlib.import_module("42cli.authorize")
api = importlib.import_module("42cli.api")
const = importlib.import_module("42cli.const")


def cloneProject():
    authInfo = authorize.getAuthInfo()
    apiResponse = api.apiGetUsers(authInfo)

    choices = {}
    for project in apiResponse['projects_users']:
        choices[project['project']['name']] = project['id']

    questions = [
        inquirer.List(
            "repo",
            message="What project do you want to clone?",
            choices=choices.keys(),
            carousel=True,
        )
    ]

    answer = inquirer.prompt(questions)
    projectName = answer['repo']

    apiResponse = api.apiGetProjectsUsers(authInfo, choices[answer['repo']])

    if len(apiResponse['teams']) > 1:
        choices = {}
        for project in apiResponse['teams']:
            choices[project['name']] = project['repo_url']

        questions = [
            inquirer.List(
                "repo",
                message="What project do you want to clone?",
                choices=choices.keys(),
                carousel=True,
            )
        ]

        answer = inquirer.prompt(questions)
    else:
        answer['repo'] = apiResponse['teams'][0]['repo_url']

    try:
        git.Repo.clone_from(choices[answer['repo']], projectName)
    except git.exc.GitCommandError:
        click.secho(const.MSG_GIT_ERROR, fg='red')
        sys.exit(1)
