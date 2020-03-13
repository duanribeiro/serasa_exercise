# -*- coding: latin-1 -*-

from api.tests.conftest import client
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
#
# def test_run_crawler(client):
#     response = client.post('/api/v1/')
#     assert response.status_code == 200


def test_get_info_database(client):
    response = client.get('/api/v1/')

    assert response.status_code == 200
    assert response.json[0]['author'] == 'Albert Einstein'
