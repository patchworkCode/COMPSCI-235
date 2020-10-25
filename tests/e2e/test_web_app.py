import pytest

from flask import session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200

def test_movies_without_rank(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies_by_rank')
    assert response.status_code == 200



def test_movies_with_rank(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies_by_rank?rank=2')
    assert response.status_code == 200


#end here

