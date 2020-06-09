#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import importlib
import os
import sys

import click

from definitions import ROOT_DIR
const = importlib.import_module('42cli.const')


def openFileToWrite(path, content):
    with open(path, 'wb') as fp:
        pickle.dump(content, fp)


def openFileToRead(path):
    with open(path, 'rb') as fp:
        return pickle.load(fp)


def getConfig():
    return openFileToRead(ROOT_DIR+'/'+const.CONFIG_FILE)


def getCache():
    return openFileToRead(ROOT_DIR+'/'+const.CACHE_FILE)


def checkConfigExists():
    if not os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
        click.secho(const.MSG_NO_CONFIG_FOUND, fg='red')
        sys.exit(1)
