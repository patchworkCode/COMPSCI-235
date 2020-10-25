import pytest


from A3.utilities import services as news_services

from A3.utilities.services import NonExistentmovieException

def test_get_first_movie(in_memory_repo):
    movie_as_dict = news_services.get_first_movie(in_memory_repo)

    assert movie_as_dict['rank'] == 1


def test_get_last_movie(in_memory_repo):
    movie_as_dict = news_services.get_last_movie(in_memory_repo)

    assert movie_as_dict['rank'] == 6


def test_get_movies_by_rank_with_one_rank(in_memory_repo):
    target_rank = 1

    movies_as_dict, prev_rank, next_rank = news_services.get_movies_by_rank(target_rank, in_memory_repo)
    assert len(movies_as_dict) == 1
    assert movies_as_dict[0]['rank'] == 1

    assert prev_rank is None
    assert next_rank == 2

def test_get_movies_by_rank_with_non_existent_rank(in_memory_repo):
    target_rank = 20

    movies_as_dict, prev_rank, next_rank = news_services.get_movies_by_rank(target_rank, in_memory_repo)

    # Check that there are no movies rankd 2020-03-06.
    assert len(movies_as_dict) == 0



