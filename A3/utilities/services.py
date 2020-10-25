from typing import Iterable

from A3.adapters.repository import AbstractRepository
from A3.domainmodel.movie import Movie

class NonExistentmovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentmovieException

    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)


def get_movies_by_rank(rank, repo: AbstractRepository):
    movies = repo.get_movies_by_rank(target_rank=rank)

    movies_dto = list()
    prev_rank = next_rank = None

    if len(movies) > 0:
        prev_rank = repo.get_rank_of_previous_movie(movies[0])
        next_rank = repo.get_rank_of_next_movie(movies[0])
        movies_dto = movies_to_dict(movies)

    return movies_dto, prev_rank, next_rank


def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.movie_title,
        'year': movie.movie_year,
        'rank': movie.rank
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def dict_to_movie(dict):
    movie = Movie(dict.title, dict.year, dict.rank)
    # Note there's no comments or tags.
    return movie

