#!/usr/bin/env python
# -*- coding: utf=8 -*-

import click

import fortytwocli.init as init_
import fortytwocli.status as status_
import fortytwocli.project as project
import fortytwocli.util as util


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
        project.cloneProject()
    except Exception as e:
        click.secho(str(e), fg='red')


def main():
    fourtyTwo()
