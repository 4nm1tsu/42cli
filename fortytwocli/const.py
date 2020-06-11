#!/usr/bin/env python
# -*- coding: utf=8 -*-

import os

MSG_NO_PROJECT_IN_PROGRESS = "There's no projects in progress."
MSG_NO_AVAILABLE_REPO = "Sorry... There's no clonable repository."
MSG_GIT_ERROR = "ERROR: Please make sure you have the correct access rights\
 and the repository exists."
MSG_API_ACCESS_ERROR = "ERROR: An error has occurred during accessing API."
MSG_AUTHORIZE_ERROR = "ERROR: An error has occurred during authorization."
MSG_NO_CONFIG_FOUND_ERROR = """no config file found.
please use '42 init' command to finish settings.
"""
MSG_REQUEST_TOKEN = "requesting access token..."
MSG_ACCESSING_API = "accessing the resources..."
MSG_CONFIG_SAVED = "changes have been saved!"
FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
CONFIG_FILE = FILE_PATH+"config.dat"
CACHE_FILE = FILE_PATH+"cache.dat"
