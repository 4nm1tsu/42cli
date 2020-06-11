#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import pickle
import os
from unittest import mock

import pytest

init_ = importlib.import_module("fortytwocli.init")
const = importlib.import_module("fortytwocli.const")


@pytest.fixture
def api_config():
    return init_.Config('foo', 'bar', 'baz')


class Testinit_():
    @classmethod
    def setup_class(cls):
        if os.path.exists(const.CONFIG_FILE):
            os.remove(const.CONFIG_FILE)

    def teardown_method(self, method):
        if os.path.exists(const.CONFIG_FILE):
            os.remove(const.CONFIG_FILE)

    @mock.patch('fortytwocli.init.inquirer.prompt')
    def test_init(self, inquirerMock, api_config):
        inquirerMock.return_value = {
            'uid': 'foo',
            'secret': 'bar',
            'username': 'baz',
        }
        init_.init()
        with open(const.CONFIG_FILE, 'rb') as fp:
            config = pickle.load(fp)
        assert api_config.uid == config.uid
        assert api_config.secret == config.secret
        assert api_config.username == config.username


if __name__ == '__main__':
    pytest.main()
