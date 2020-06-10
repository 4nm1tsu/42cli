#!/usr/bin/env python
# -*- coding: utf=8 -*-


class GitError(Exception):
    pass


class ApiAccessError(Exception):
    pass


class AuthorizeError(Exception):
    pass


class NoConfigFoundError(Exception):
    pass
