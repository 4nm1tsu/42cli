#!/usr/bin/env python
# -*- coding: utf=8 -*-

import click

from . import init as it


@click.group()
def fourty_two():
    pass


@fourty_two.command(help="initialize settings.")
def init():
    it.init()


@fourty_two.command(help="show your status.")
def status():
    pass


@fourty_two.command(help="show your review schedule.")
def review():
    pass


@fourty_two.command(help="show your available projects.")
def project():
    pass


def main():
    fourty_two()
