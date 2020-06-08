#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle

import click
import inquirer

from definitions import ROOT_DIR


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
    with open(ROOT_DIR+'/config.dat', 'wb') as fp:
        pickle.dump(config, fp)
    click.secho("changes have been saved!", fg='green')
