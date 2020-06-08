#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import os
import sys

import click

from definitions import ROOT_DIR
const = importlib.import_module("42cli.const")
init_ = importlib.import_module("42cli.init")
show_username = importlib.import_module("42cli.show_username")


def checkConfigExists():
    if not os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
        click.secho(const.MSG_NO_CONFIG_FOUND, fg='red')
        sys.exit(1)


@click.group()
def fourtyTwo():
    pass


@fourtyTwo.command(help="initializes settings.")
def init():
    init_.init()


@fourtyTwo.command(help="shows your status.")
def status():
    checkConfigExists()
    show_username.showUserName()


@fourtyTwo.command(help="shows your review schedule.")
def review():
    checkConfigExists()


@fourtyTwo.command(help="shows your available projects.")
def project():
    checkConfigExists()


def main():
    fourtyTwo()
