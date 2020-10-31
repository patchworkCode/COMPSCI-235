import pytest
from A3.adapters.database_repository import SqlAlchemyRepository

from sqlalchemy.exc import IntegrityError

from A3.domainmodel.movie import Movie

movie_rank = 2
movie_year = 2012


def insert_movie(empty_session):
    empty_session.execute(
        'INSERT INTO movies (title) VALUES '
        '"test"')
    row = empty_session.execute('SELECT rank from movies').fetchone()
    return row[0]




def make_movie():
    movie = Movie(
        movie_rank, 'test', movie_year
    )
    return movie



def test_loading_of_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(1)

    # Check that the movie has the expected title.

    assert movie._rank == 1


def test_saving_of_movie(empty_session):
    movie = make_movie()
    empty_session.add(movie)
    empty_session.commit()

    rows = list(empty_session.execute('SELECT rank, title, 2012 from movies'))
    rank = movie_rank
    year = movie_year
    assert rows == [(rank,
                     "test",
                     year
                     )]
