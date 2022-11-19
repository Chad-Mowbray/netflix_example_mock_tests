import unittest
from src.movie import Movie

class TestMovie(unittest.TestCase):

    def test_movie_init(self):
        movie_id = 123
        m = Movie("asdf", movie_id)
        self.assertEqual(movie_id, m.id)