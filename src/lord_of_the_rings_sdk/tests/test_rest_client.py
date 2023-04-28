import unittest
import requests_mock
import json

from lord_of_the_rings_sdk.rest import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_json_response = json.dumps({
            "docs": [
                {
                    "_id": "5cd95395de30eff6ebccde56",
                    "name": "The Lord of the Rings Series",
                    "runtimeInMinutes": 558,
                    "budgetInMillions": 281,
                    "boxOfficeRevenueInMillions": 2917,
                    "academyAwardNominations": 30,
                    "academyAwardWins": 17,
                    "rottenTomatoesScore": 94
                }
            ]})

    @requests_mock.Mocker()
    def test_request(self, m):
        m.get(
            'https://the-one-api.dev/v2/movie', json=self.mock_json_response)
        response = self.client.request('movie')
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['json'], self.mock_json_response)

    def test_movie_property_returns_movie_instance(self):
        movie = self.client.movie
        from rest.movie import Movie
        self.assertIsInstance(movie, Movie)

    def test_quote_property_returns_quote_instance(self):
        quote = self.client.quote
        from rest.quote import Quote
        self.assertIsInstance(quote, Quote)

if __name__ == '__main__':
    unittest.main()
