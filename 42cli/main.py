#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import click

# import init as init_
init_ = importlib.import_module("42cli.init")


@click.group()
def fourty_two():
    pass


@fourty_two.command(help="initializes settings.")
def init():
    init_.init()


@fourty_two.command(help="shows your status.")
def status():
    pass


@fourty_two.command(help="shows your review schedule.")
def review():
    pass


@fourty_two.command(help="shows your available projects.")
def project():
    pass


def main():
    fourty_two()
