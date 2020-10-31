import csv
import os
from bisect import bisect_left, insort_left
from typing import List

from A3.adapters.repository import AbstractRepository
from A3.domainmodel.movie import Movie


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self._movies = list()
        self._movies_index = dict()

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.rank] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None

        try:
            movie = self._movies_index[id]
        except KeyError:
            pass

        return movie

    def get_movies_by_rank(self, target_rank) -> List[Movie]:
        matching_movies = list()
        try:
            for movie in self._movies:
                if int(movie.rank) == int(target_rank):
                    matching_movies.append(movie)
        except ValueError:
            pass
        return matching_movies

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_rank_of_previous_movie(self, movie: Movie):
        previous_rank = None

        try:
            index = self.movie_index(movie)
            for stored_movie in reversed(self._movies[0:index]):
                if stored_movie.rank < movie.rank:
                    previous_rank = stored_movie.rank
                    break
        except ValueError:
            pass
        return previous_rank

    def get_rank_of_next_movie(self, movie: Movie):
        next_rank = None

        try:
            index = self.movie_index(movie)
            for stored_movie in self._movies[index + 1:len(self._movies)]:
                if stored_movie.rank > movie.rank:
                    next_rank = stored_movie.rank
                    break
        except ValueError:
            # No subsequent movies, so return None.
            pass

        return next_rank

    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        return index


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            yield row


def load_movies_and_tags(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies')):
        movie = Movie(
            movie_title=data_row[1],
            movie_year=int(data_row[6]),
            rank=int(data_row[0])
        )
        # Add the Article to the repository.
        repo.add_movie(movie)


def populate(data_path: str, repo: MemoryRepository):
    load_movies_and_tags(data_path, repo)
