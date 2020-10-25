from datetime import date

from A3.domainmodel.movie import Movie

import pytest


@pytest.fixture()
def movie():
    return Movie(
        1,
        'test_movie2',
        2012
    )


def test_article_construction(movie):
    assert movie.rank == 1
    assert movie.movie_title == 'test_movie2'
    assert movie.movie_year == 2012

    assert repr(
        movie) == '<Movie test_movie2, 2012>'


def test_article_less_than_operator():
    article_1 = Movie(
        2, 'test_movie3', 2011
    )

    article_2 = Movie(
        3, 'test_move4', 2015
    )

    assert article_1 < article_2

