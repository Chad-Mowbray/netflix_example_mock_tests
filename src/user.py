from src.movies_api import MoviesAPI
from src.saved_movies import SavedMovies


class User:

    def __init__(self, uname):
        self.uname = uname
        self.movies_api = MoviesAPI()
        self.saved_movies = SavedMovies()

    def save_movie(self):
        # Get a random movie
        movie = self.movies_api.fetch_movie()
        self.saved_movies.add_movie(movie)

    def watch_saved_movie(self, movie_id):
        try:
            movie_to_watch = self.saved_movies.remove_movie(movie_id)
            print(f"You are watching {movie_to_watch.title}")
        except ValueError:
            print("You haven't saved that movie yet")

        # if movie_to_watch:
        #     print(f"You are watching {movie_to_watch.title}")
        # else:
        #     print("You haven't saved that movie yet")
        