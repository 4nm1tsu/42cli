#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import os

import click
import inquirer
from rich.console import Console
from rich.table import Table

from definitions import ROOT_DIR


class Config:
    def __init__(self, uid: str, secret: str):
        self.uid = uid
        self.secret = secret


def configSet():
    questions = [
        inquirer.Text('uid', message='Paste your UID'),
        inquirer.Text('secret', message='Paste your SECRET'),
    ]
    answers = inquirer.prompt(questions)
    config = Config(**answers)
    with open(ROOT_DIR+'/config.dat', 'wb') as fp:
        pickle.dump(config, fp)
    click.secho("changes have been saved!", fg='green')


def configGet(set: bool):
    try:
        with open(ROOT_DIR+'/config.dat', 'rb') as fp:
            config = pickle.load(fp)
    except FileNotFoundError:
        if not set:
            click.secho("You've not set up API settings!", fg='red', err=True)
            click.secho("Set up API settings via '42 config --set' command.",
                        fg='red', err=True)
    else:
        click.secho('Your current API configuration', fg='bright_green')
        console = Console()
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column('UID')
        table.add_column('SECRET')
        table.add_row(
            config.uid,
            config.secret,
        )
        console.print(table)


def configDelete():
    if os.path.exists(ROOT_DIR+'/config.dat'):
        questions = [
            inquirer.Confirm('continue',
                             message="Are you sure you want to"
                             + "delete current configuration?"),
        ]
        answer = inquirer.prompt(questions)
        if answer['continue']:
            try:
                os.remove(ROOT_DIR+'/config.dat')
            except Exception:
                pass
            else:
                click.secho('delete success!', fg='green')
    else:
        click.secho('configuration does not exist.', fg='red', err=True)
