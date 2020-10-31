class Movie:
    def __init__(self, rank: int, movie_title: str, movie_year: int):
        # TITLE
        if movie_title == "" or type(movie_title) is not str:
            self.movie_title = None
        else:
            self.movie_title = movie_title.strip()

        # YEAR
        if movie_year == "" or type(movie_year) is not int:
            self.movie_year = None
        elif movie_year < 1900:
            raise ValueError("ValueError exception thrown: Year is < 1900")
        else:
            self.movie_year = movie_year

        #rank
        if rank == "" or type(rank) is not int:
            self._rank = 0
        else:
            self._rank = rank

        self._description = None
        self._director = None
        self._actors = None
        self._genres = None
        self._runtime_minutes = 0


    @property
    def rank(self):
        return self._rank

    # DESCRIPTION
    @property
    def description(self):
        return self._description

    # DIRECTOR
    @property
    def director(self):
        return self._director

    # ACTORS
    @property
    def actors(self):
        return self._actors

    # GENRES
    @property
    def genres(self):
        return self._genres

    # RUNTIME_MINUTES
    @property
    def runtime_minutes(self):
        return self._runtime_minutes


    # @property
    def __repr__(self):
        return f"<Movie {self.movie_title}, {self.movie_year}>"

    def __eq__(self, other):
        # TODO
        return self.movie_title == other.movie_title and self.movie_year == other.movie_year

    def __lt__(self, other):
        # TODO
        if self.movie_title == other.movie_title:
            return self.movie_year < other.movie_year
        else:
            return self._rank < other._rank

    def __hash__(self):
        # TODO
        return hash((self.movie_title, self.movie_year))

    def add_actor(self, actor_obj):
        if actor_obj not in self.actors:
            self.actors.append(actor_obj)

    def remove_actor(self, actor_obj):
        if actor_obj in self.actors:
            self.actors.remove(actor_obj)

    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.genres:
            self.genres.remove(genre)

    @description.setter
    def description(self, text):
        if text == "" or type(text) is not str:
            self._description = None
        else:
            self._description = text.strip()

    @director.setter
    def director(self, name):
        self._director = name

    @actors.setter
    def actors(self, actors_obj):
        self._actors = actors_obj

    @genres.setter
    def genres(self, genre_obj):
        self._genres = genre_obj

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if runtime < 0:
            raise ValueError("ValueError exception thrown: Not positive")
        else:
            self._runtime_minutes = runtime
