import pytest

from A3.adapters.database_repository import SqlAlchemyRepository
from A3.domainmodel.movie import Movie
from A3.adapters.repository import RepositoryException

def test_repository_can_retrieve_movie_count(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    number_of_movies = repo.get_number_of_movies()

    # Check that the query returned 177 movies.
    assert number_of_movies == 6

def test_repository_can_add_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    number_of_movies = repo.get_number_of_movies()

    new_movie_rank = number_of_movies + 1

    movie = Movie(
        new_movie_rank,
        'test1',
        2012,
    )
    repo.add_movie(movie)

    assert repo.get_movie(new_movie_rank) == movie

def test_repository_can_retrieve_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(1)

    # Check that the movie has the expected title.
    assert movie.movie_title == 'Guardians of the Galaxy'


def test_repository_does_not_retrieve_a_non_existent_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(201)
    assert movie is None

def test_repository_can_retrieve_movies_by_rank(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movies = repo.get_movies_by_rank(3)

    # Check that the query returned 1 movies.
    assert len(movies) == 1


def test_repository_can_get_first_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_first_movie()
    assert movie.movie_title == 'Guardians of the Galaxy'

def test_repository_can_get_last_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_last_movie()
    assert movie.movie_title == 'The Great Wall'


def test_repository_returns_rank_of_previous_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(6)
    previous_rank = repo.get_rank_of_previous_movie(movie)

    assert previous_rank == 5


def test_repository_returns_none_when_there_are_no_previous_movies(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(1)
    previous_rank = repo.get_rank_of_previous_movie(movie)

    assert previous_rank is None


def test_repository_returns_rank_of_next_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(3)
    next_rank = repo.get_rank_of_next_movie(movie)

    assert next_rank == 4


def test_repository_returns_none_when_there_are_no_subsequent_movies(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movie = repo.get_movie(7)
    next_rank = repo.get_rank_of_next_movie(movie)

    assert next_rank is None

def make_movie(new_movie_rank):
    movie = Movie(
        new_movie_rank,
        'test2',
        2011,
    )
    return movie


