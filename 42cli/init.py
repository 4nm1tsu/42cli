#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle

import click
import inquirer

from definitions import ROOT_DIR


MSG_CONFIG_SAVED = "changes have been saved!"
CONFIG_FILE = "config.dat"


class Config:
    def __init__(self, uid: str, secret: str):
        self.uid = uid
        self.secret = secret


def init():
    questions = [
        inquirer.Text('uid', message='Paste UID'),
        inquirer.Text('secret', message='Paste SECRET'),
    ]
    answers = inquirer.prompt(questions)
    config = Config(**answers)
    with open(ROOT_DIR+'/'+CONFIG_FILE, 'wb') as fp:
        pickle.dump(config, fp)
    click.secho(MSG_CONFIG_SAVED, fg='green')
