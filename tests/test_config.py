#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
import pickle
import os

import pytest

from definitions import ROOT_DIR

config = importlib.import_module("42cli.config")


@pytest.fixture
def api_config():
    return config.Config('hoge', 'fuga')


class TestConfig():
    @classmethod
    def setup_class(cls):
        if os.path.exists(ROOT_DIR+'/config.dat'):
            os.remove(ROOT_DIR+'/config.dat')

    def teardown_method(self, method):
        if os.path.exists(ROOT_DIR+'/config.dat'):
            os.remove(ROOT_DIR+'/config.dat')

    def test_configGet(self, api_config, capfd):
        # config fileが存在しない場合
        config.configGet(False)
        out, err = capfd.readouterr()
        assert len(out) == 0
        assert "You've not set up API settings!" in err

        # config fileが存在する場合
        # config file 作成
        with open(ROOT_DIR+'/config.dat', 'wb') as fp:
            pickle.dump(api_config, fp)
        config.configGet(True)
        out, err = capfd.readouterr()
        assert 'hoge' in out
        assert 'fuga' in out
        assert len(err) == 0

    def test_configDelete(self, capfd):
        # config fileが存在しない場合
        config.configDelete()
        out, err = capfd.readouterr()
        assert "configuration does not exist." in err

        # config fileが存在する場合
        # config file 作成
        with open(ROOT_DIR+'/config.dat', 'wb') as fp:
            pickle.dump(api_config, fp)
        #config.configDelete()
        #out, err = capfd.readouterr()

        #assert os.path.exists(ROOT_DIR+'/config.dat')

    def test_configCommand(self):
        pass


if __name__ == '__main__':
    pytest.main()
