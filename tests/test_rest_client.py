import unittest
from dotenv import load_dotenv
import os
from rest import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    # def test_request_calls_api_requester(self):
    #     # Create a temporary .env file
    #     with open('.env.test', 'w') as f:
    #         f.write('LOTR_API_BASE_URL=https://example.com\n')
    #         f.write('LOTR_AUTH_BEARER_TOKEN=abc123\n')
        
        

    #     # Load the environment variables from the temporary .env file
    #     load_dotenv('.env.test')

    #     # Call the `request` method with some arguments
    #     content_type = 'movie'
    #     params = {'foo': 'bar'}
    #     headers = {'Authorization': 'Bearer abc123'}
    #     response = self.client.request(
    #         content_type=content_type,
    #         params=params,
    #         headers=headers,
    #     )

    #     # Check that the `request` method returns the expected response
    #     self.assertEqual(response['status'], 200)
    #     self.assertEqual(response['json'], {'foo': 'bar'})

    #     # Remove the temporary .env file
    #     os.remove('.env.test')

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
