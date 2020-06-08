#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import pickle
import os

import pytest

from definitions import ROOT_DIR
init_ = importlib.import_module("42cli.init")
# from 42cli.init import CONFIG_FILE


@pytest.fixture
def api_config():
    return init_.Config('hoge', 'fuga')


class Testinit_():
    @classmethod
    def setup_class(cls):
        if os.path.exists(ROOT_DIR+'/'+init_.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+init_.CONFIG_FILE)

    def teardown_method(self, method):
        if os.path.exists(ROOT_DIR+'/'+init_.CONFIG_FILE):
            os.remove(ROOT_DIR+'/'+init_.CONFIG_FILE)

    def test_init(self, api_config, capfd):
        # init_.init()
        pass


if __name__ == '__main__':
    pytest.main()
