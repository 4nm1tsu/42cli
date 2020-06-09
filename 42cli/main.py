#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

import click

const = importlib.import_module("42cli.const")
init_ = importlib.import_module("42cli.init")
status_ = importlib.import_module("42cli.status")
project_ = importlib.import_module("42cli.project")
util = importlib.import_module("42cli.util")


@click.group()
def fourtyTwo():
    pass


@fourtyTwo.command(help="initializes settings.")
def init():
    init_.init()


@fourtyTwo.command(help="shows your status.")
def status():
    util.checkConfigExists()
    status_.showStatus()


@fourtyTwo.command(help="shows your review schedule.")
def review():
    util.checkConfigExists()


@fourtyTwo.command(name="clone-project", help="clone project.")
def clone_project():
    util.checkConfigExists()
    project_.cloneProject()


def main():
    fourtyTwo()
