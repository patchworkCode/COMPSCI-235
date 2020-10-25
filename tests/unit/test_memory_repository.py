from A3.domainmodel.movie import Movie
from A3.adapters.repository import RepositoryException


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 6 movies.
    assert number_of_movies == 6


def test_repository_can_add_movie(in_memory_repo):
    test = Movie(
        7,
        "cool_movie",
        2016
    )
    in_memory_repo.add_movie(test)

    assert in_memory_repo.get_movie(7) is test


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)

    # Check that the movie has the expected title.
    assert movie.movie_title == 'Guardians of the Galaxy'


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(101)
    assert movie is None


def test_repository_can_get_movies_by_rank(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank(3)

    # Check that the query returned 3 movies.
    assert len(movies) == 1


def test_repository_does_not_retrieve_a_movie_when_there_are_no_movies_for_a_given_rank(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank(1001)
    assert len(movies) == 0


def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.movie_title == 'Guardians of the Galaxy'


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.movie_title == 'The Great Wall'


def test_repository_returns_rank_of_previous_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(6)
    previous_rank = in_memory_repo.get_rank_of_previous_movie(movie)

    assert previous_rank == 5


def test_repository_returns_none_when_there_are_no_previous_movies(in_memory_repo):
    movie = in_memory_repo.get_movie(1)
    previous_rank = in_memory_repo.get_rank_of_previous_movie(movie)

    assert previous_rank is None


def test_repository_returns_rank_of_next_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(3)
    next_rank = in_memory_repo.get_rank_of_next_movie(movie)

    assert next_rank == 4


def test_repository_returns_none_when_there_are_no_subsequent_movies(in_memory_repo):
    movie = in_memory_repo.get_movie(6)
    next_rank = in_memory_repo.get_rank_of_next_movie(movie)

    assert next_rank is None





