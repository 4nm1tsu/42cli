#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib

import pytest

config = importlib.import_module("42cli.config")


@pytest.fixture
def something():
    return {
        'hoge': 'fuga',
    }


class TestConfig():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    """
@pytest.mark.parametrize("x,y,sum", [
    (1, 2, 3),
    (2, 3, 5),
])
def test_add(x, y, sum):
    assert (x + y) == sum
    """

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_something(self):
        pass


if __name__ == '__main__':
    pytest.main()
