#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import importlib

import click
import inquirer

const = importlib.import_module('fortytwocli.const')


class Config:
    def __init__(self, uid: str, secret: str, username: str):
        self.uid = uid
        self.secret = secret
        self.username = username


def init():
    questions = [
        inquirer.Text('uid', message='Paste UID'),
        inquirer.Text('secret', message='Paste SECRET'),
        inquirer.Text('username', message="What's your login name?"),
    ]
    answers = inquirer.prompt(questions)
    config = Config(**answers)
    with open(const.CONFIG_FILE, 'wb') as fp:
        pickle.dump(config, fp)
    click.secho(const.MSG_CONFIG_SAVED, fg='green')
