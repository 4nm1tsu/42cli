#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import pickle
import os
from unittest import mock

import pytest

from definitions import ROOT_DIR
init_ = importlib.import_module("fortytwocli.init")
const = importlib.import_module("fortytwocli.const")


@pytest.fixture
def api_config():
    return init_.Config('hoge', 'fuga', 'username')


class Testinit_():
    @classmethod
    def setup_class(cls):
        if os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+const.CONFIG_FILE)

    def teardown_method(self, method):
        if os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+const.CONFIG_FILE)

    @mock.patch('fortytwocli.init.inquirer.prompt')
    def test_init(self, inquirerMock, api_config):
        pass


if __name__ == '__main__':
    pytest.main()
