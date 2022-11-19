

class SavedMovies:

    def __init__(self):
        self.storage = []

    def add_movie(self, movie):
        self.storage.append(movie)

    def remove_movie(self, movie_id):
        # search in self.storage for movie_id
        for idx,movie in enumerate(self.storage):
            if movie.id == movie_id:
                # if found, remove and return the movie
                found_movie = self.storage.pop(idx)
                return found_movie   
        raise ValueError("Movie not Found")     


    def show_movies(self):
        if not self.storage: print("no movies...")
        for movie in self.storage:
            print(movie)