import unittest
from src.user import User
from src.movie import Movie

from unittest.mock import patch, MagicMock

class FakeMoviesAPI:
    def fetch_movie(self):
        return Movie("asd", 123)

class TestUser(unittest.TestCase):

    def test_save_movie(self):
        u = User("bob")
        u.movies_api = FakeMoviesAPI()
        u.save_movie()
        self.assertEqual(len(u.saved_movies.storage), 1)

    def test_save_movie2(self):
        u = User("bob")
        u.movies_api.fetch_movie = lambda : Movie("asd", 123)
        u.save_movie()
        self.assertEqual(len(u.saved_movies.storage), 1)

    @patch("src.movies_api.requests")
    def test_save_movie3(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "name": "movie",
            "equipment": "stuff",
            "id": 123
        }
        mock_response.get.return_value = mock_response

        u = User("bob")
        u.save_movie()
        self.assertEqual(len(u.saved_movies.storage), 1)    