#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

import click

const = importlib.import_module("fortytwocli.const")
init_ = importlib.import_module("fortytwocli.init")
status_ = importlib.import_module("fortytwocli.status")
project_ = importlib.import_module("fortytwocli.project")
util = importlib.import_module("fortytwocli.util")


@click.group()
def fourtyTwo():
    pass


@fourtyTwo.command(help="initializes settings.")
def init():
    init_.init()


@fourtyTwo.command(help="shows your status.")
def status():
    try:
        util.checkConfigExists()
        status_.showStatus()
    except Exception as e:
        click.secho(str(e), fg='red')


@fourtyTwo.command(name="clone-project", help="clone project.")
def clone_project():
    try:
        util.checkConfigExists()
        project_.cloneProject()
    except Exception as e:
        click.secho(str(e), fg='red')


def main():
    fourtyTwo()
