from A3.domainmodel.movie import Movie

class WatchList:
    [[
         "watchlist = WatchList()\nprint(f\"Size of watchlist: {watchlist.size()}\")\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nwatchlist.add_movie(Movie(\"Guardians of the Galaxy\", 2012))\nprint(watchlist.first_movie_in_watchlist())",
         "Size of watchlist: 0\n<Movie Moana, 2016>"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nfor movie in watchlist:\n    print(movie)",
         "<Movie Moana, 2016>\n<Movie Ice Age, 2002>"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nprint(watchlist.size())",
         "2"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nwatchlist.remove_movie(Movie(\"Moana\", 2016))\nfor movie in watchlist:\n    print(movie)",
         "<Movie Ice Age, 2002>"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nwatchlist.remove_movie(Movie(\"Moana\", 2016))\nfor movie in watchlist:\n    print(movie)",
         "<Movie Ice Age, 2002>"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nindex = 1\nprint(watchlist.select_movie_to_watch(index))",
         "<Movie Ice Age, 2002>"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nindex = 4\nprint(watchlist.select_movie_to_watch(index))",
         "None"], [
         "watchlist = WatchList()\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nwatchlist.add_movie(Movie(\"Ice Age\", 2002))\nwatchlist.add_movie(Movie(\"Guardians of the Galaxy\", 2012))\nwatchlist.add_movie(Movie(\"Moana\", 2016))\nfor movie in watchlist:\n    print(movie)",
         "<Movie Moana, 2016>\n<Movie Ice Age, 2002>\n<Movie Guardians of the Galaxy, 2012>"], ["", ""], ["", ""]]