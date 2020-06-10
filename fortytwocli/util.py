#!/usr/bin/env python
# -*- coding: utf=8 -*-

import pickle
import importlib
import os

from definitions import ROOT_DIR
const = importlib.import_module("fortytwocli.const")
exception = importlib.import_module("fortytwocli.exception")


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
        raise exception.NoConfigFoundError(const.MSG_NO_CONFIG_FOUND_ERROR)
