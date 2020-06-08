#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import pickle
import os
from unittest import mock

import pytest

from definitions import ROOT_DIR
init_ = importlib.import_module("42cli.init")
const = importlib.import_module("42cli.const")


@pytest.fixture
def api_config():
    return init_.Config('hoge', 'fuga')


class Testinit_():
    @classmethod
    def setup_class(cls):
        if os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+const.CONFIG_FILE)

    def teardown_method(self, method):
        if os.path.exists(ROOT_DIR+'/'+const.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+const.CONFIG_FILE)

    @mock.patch('42cli.init.inquirer.prompt')
    def test_init(self, inquirerMock, api_config):
        inquirerMock.return_value = {
            'uid': 'hoge',
            'secret': 'fuga',
        }
        init_.init()
        with open(ROOT_DIR+'/'+const.CONFIG_FILE, 'rb') as fp:
            config = pickle.load(fp)
        assert api_config.uid == config.uid
        assert api_config.secret == config.secret


if __name__ == '__main__':
    pytest.main()
