from A3.domainmodel.genre import Genre
from A3.domainmodel.actor import Actor
from A3.domainmodel.director import Director

class Movie:
    def __init__(self, title: str, date: int):
        self.__genres = []
        self.__actors = []
        self.__runtime_minutes = 0
        self.__director = Director("")
        self.__description = None
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if date == "" or type(date) is not int:
            self.__date = None
        else:
            if date < 1900:
                self.__date = None
            else:
                self.__date = date

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description):
        if type(new_description) is str:
            self.__description = new_description

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director):
        if type(new_director) is Director:
            self.__director = new_director

    @property
    def runtime_minutes(self) -> int:

        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if type(runtime) is int:
            if runtime < 0:
                raise ValueError
            else:
                self.__runtime_minutes = runtime

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) is str and title != "":
            self.__title = title.strip()

    @property
    def date(self) -> int:
        return self.__date

    @date.setter
    def date(self, date):
        if type(date) is not int:
            if date < 1900:
                self.__date = None
            else:
                self.__date = date

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, new_list):
        if type(new_list) == list:
            self.__genres = new_list

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, new_list):
        if type(new_list) == list:
            self.__actors = new_list

    def __repr__(self):
        return f"<Movie {self.title}, {self.date}>"

    def __eq__(self, other):
        if self.title == other.title and self.date == other.date:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__date < other.__date
        else:
            return self.__title < other.__title

    def __hash__(self):
        return hash(self.title)

    def add_actor(self, actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

def main():
    movie = Movie("Moana", 2016)
    movie2 = Movie("Moana", 1999)
    print("here", movie2 < movie)
    print(movie)

    director = Director("Ron Clements")
    movie.director = director
    print(movie.director)

    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    print(movie.actors)

    movie.runtime_minutes = 107
    print("Movie runtime: {} minutes".format(movie.runtime_minutes))
main()