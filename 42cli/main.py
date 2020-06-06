#!/usr/bin/env python
# -*- coding: utf=8 -*-

import click

from . import config as cf


@click.group()
def fourty_two():
    pass


@fourty_two.command(help="show, set or delete current API configuration.")
@click.option('--set', '-s',
              is_flag=True,
              help="set values of API configuration.")
@click.option('--delete', '-d',
              is_flag=True,
              help="delete current API configuration.")
def config(set, delete):
    if set and delete:
        click.secho("You can't use these options at the same time.",
                    fg='red',
                    err=True)
        return
    if not delete:
        cf.configGet(set)
    if set:
        cf.configSet()
    if delete:
        cf.configDelete()


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
