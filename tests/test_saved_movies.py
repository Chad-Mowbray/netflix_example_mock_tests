import unittest
from src.saved_movies import SavedMovies
from src.movie import Movie

class TestSavedMovies(unittest.TestCase):

    def test_add_movie(self):
        sm = SavedMovies()
        m = Movie("asdf", 123)
        sm.add_movie(m)
        self.assertEqual(len(sm.storage), 1)