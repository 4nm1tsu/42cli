#!/usr/bin/env python
# -*- coding: utf=8 -*-

import importlib
from unittest import mock

import pytest

project = importlib.import_module("42cli.project")
const = importlib.import_module("42cli.const")
exception = importlib.import_module("42cli.exception")


@pytest.fixture
def api_config():
    pass


class TestProject():
    @mock.patch('42cli.init.inquirer.prompt')
    @mock.patch("42cli.api.apiGetProjectsUsers")
    @mock.patch("42cli.api.apiGetUsers")
    @mock.patch("42cli.authorize.getAuthInfo")
    def test_cloneProject(
        self,
        getAuthInfoMock,
        apiGetUsersMock,
        apiGetProjectsUsersMock,
        inquirerMock,
        capfd
    ):
        getAuthInfoMock.return_value = "hoge"
        apiGetUsersMock.return_value = {
            "id": 2,
            "email": "andre@42.fr",
            "login": "andre",
            "first_name": "André",
            "last_name": "Aubin",
            "url": "https://api.intra.42.fr/v2/users/andre",
            "phone": None,
            "displayname": "André Aubin",
            "image_url": "https://cdn.intra.42.fr/images/default.png",
            "staff?": False,
            "correction_point": 4,
            "pool_month": "july",
            "pool_year": "2016",
            "location": None,
            "wallet": 0,
            "anonymize_date": "2021-02-20T00:00:00.000+03:00",
            "groups": [],
            "cursus_users": [
                {
                    "id": 2,
                    "begin_at": "2017-05-14T21:37:50.172Z",
                    "end_at": None,
                    "grade": None,
                    "level": 0.0,
                    "skills": [],
                    "cursus_id": 1,
                    "has_coalition": True,
                    "user": {
                        "id": 2,
                        "login": "andre",
                        "url": "https://api.intra.42.fr/v2/users/andre"
                    },
                    "cursus": {
                        "id": 1,
                        "created_at": "2017-11-22T13:41:00.750Z",
                        "name": "Piscine C",
                        "slug": "piscine-c"
                    }
                }
            ],
            "projects_users": [
                {'current_team_id': 3022863,
                 'cursus_ids': [9],
                 'final_mark': 100,
                 'id': 1742820,
                 'marked': True,
                 'marked_at': '2020-01-09T11:10:43.490Z',
                 'occurrence': 1,
                 'project': {'id': 1256,
                             'name': 'C Piscine Shell 01',
                             'parent_id': None,
                             'slug': 'c-piscine-shell-01'},
                 'retriable_at': '2020-01-09T11:50:43.603Z',
                 'status': 'in_progress',
                 'validated?': True},
                {'current_team_id': 3022840,
                 'cursus_ids': [9],
                 'final_mark': 100,
                 'id': 1742819,
                 'marked': True,
                 'marked_at': '2020-01-09T09:36:46.835Z',
                 'occurrence': 4,
                 'project': {'id': 1255,
                             'name': 'C Piscine Shell 00',
                             'parent_id': None,
                             'slug': 'c-piscine-shell-00'},
                 'retriable_at': '2020-01-30T12:37:43.101Z',
                 'status': 'finished',
                 'validated?': True},

            ],
            "languages_users": [
                {
                    "id": 2,
                    "language_id": 3,
                    "user_id": 2,
                    "position": 1,
                    "created_at": "2017-11-22T13:41:03.638Z"
                }
            ],
            "achievements": [],
            "titles": [],
            "titles_users": [],
            "partnerships": [],
            "patroned": [
                {
                    "id": 4,
                    "user_id": 2,
                    "godfather_id": 15,
                    "ongoing": True,
                    "created_at": "2017-11-22T13:42:11.565Z",
                    "updated_at": "2017-11-22T13:42:11.572Z"
                }
            ],
            "patroning": [],
            "expertises_users": [
                {
                    "id": 2,
                    "expertise_id": 3,
                    "interested": False,
                    "value": 2,
                    "contact_me": False,
                    "created_at": "2017-11-22T13:41:22.504Z",
                    "user_id": 2
                }
            ],
            "campus": [
                {
                    "id": 1,
                    "name": "Cluj",
                    "time_zone": "Europe/Bucharest",
                    "language": {
                        "id": 3,
                        "name": "Romanian",
                        "identifier": "ro",
                        "created_at": "2017-11-22T13:40:59.468Z",
                        "updated_at": "2017-11-22T13:41:26.139Z"
                    },
                    "users_count": 28,
                    "vogsphere_id": 1
                }
            ],
            "campus_users": [
                {
                    "id": 2,
                    "user_id": 2,
                    "campus_id": 1,
                    "is_primary": True
                }
            ]
        }
        apiGetProjectsUsersMock.return_value = {
            "id": 18,
            "occurrence": 0,
            "final_mark": None,
            "status": "waiting_for_correction",
            "validated?": None,
            "current_team_id": 18,
            "project": {
                "id": 1,
                "name": "Libft",
                "slug": "libft",
                "parent_id": None
            },
            "cursus_ids": [
                1
            ],
            "user": {
                "id": 25,
                "login": "bhutt",
                "url": "https://api.intra.42.fr/v2/users/bhutt"
            },
            "teams": [
                {
                    "id": 18,
                    "name": "bhutt's group",
                    "url": "https://api.intra.42.fr/v2/teams/18",
                    "final_mark": None,
                    "project_id": 1,
                    "created_at": "2017-11-22T13:41:30.835Z",
                    "updated_at": "2017-11-22T13:41:30.920Z",
                    "status": "waiting_for_correction",
                    "terminating_at": None,
                    "users": [
                        {
                            "id": 25,
                            "login": "bhutt",
                            "url": "https://api.intra.42.fr/v2/users/bhutt",
                            "leader": True,
                            "occurrence": 0,
                            "validated": True,
                            "projects_user_id": 18
                        }
                    ],
                    "locked?": True,
                    "validated?": None,
                    "closed?": True,
                    "repo_url": 'git@vogsphere-v2.42tokyo.jp:vogsphere/intra-uuid-fa13dcf8-b055-4c3d-a4f6-e14ddcdbe827-3017110',
                    "repo_uuid": "intra-uuid-0d4153cd-21b7-4f1a-a526-297314ddc61d-18",
                    "locked_at": "2017-11-22T13:41:30.895Z",
                    "closed_at": "2017-11-22T13:41:30.919Z",
                    "project_session_id": 1
                }
            ]
        }
        inquirerMock.return_value = {
            'name': 'C Piscine Shell 01',
            'team': 'hoge',
        }
        with pytest.raises(exception.GitError):
            project.cloneProject()


if __name__ == '__main__':
    pytest.main()
