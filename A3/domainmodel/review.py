from datetime import datetime

from A3.domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, review_rating: int):
        review_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie

        if type(review_text) is not str or review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if (1 <= review_rating <= 10) == False or type(review_rating) is not int:
            self.__review_rating = None
        else:
            self.__review_rating = review_rating
        self.__timestamp = datetime.now().timestamp()

    @property
    def movie(self) -> Movie:
        return self.__movie
    @movie.setter
    def movie(self, new_movie):
        if type(new_movie) is Movie:
            self.__movie = new_movie

    @property
    def review_text(self):
        return self.__review_text
    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) is not str or review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def rating(self):
        return self.__review_rating
    @rating.setter
    def rating(self, review_rating):
        if type(review_rating) is not int or (1 <= review_rating <= 10) == False:
            self.__review_rating = None
        else:
            self.__review_rating = review_rating

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>"

    def __eq__(self, other):
        return self.__review_rating == other.__review_rating and self.__movie == other.__movie and self.__review_text == other.__review_text and self.__timestamp == other.__timestamp
"""
def main():
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)

    print(review.movie)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))
main()

"""