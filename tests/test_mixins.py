import unittest
import json

from api_utils.mixins import *


class TextMixins(unittest.TestCase):

    def setUp(self):
        self.kwargs = {
            'base_url': 'https://lordoftherings.dev',
            'version': 'v1',
            'content_type': 'movie',
            'id': '12345',
            'extra': 'quote',
            'params': {}
        }
        self.path_builder = PathBuilder(**self.kwargs)
        self.params = {"limit": "1", "page": "2", "offset": "3"}
        self.url = 'movie'

    def test_path_builder_builds_url_and_path(self):
        self.assertEqual(
            self.path_builder.build(),
            'https://lordoftherings.dev/v1/movie/12345/quote'
        )

    def test_create_params(self):
        self.assertEqual(
            create_params(url=self.url, params=json.dumps(self.params)),
            "movie?limit=1&page=2&offset=3"
        )

if __name__ == '__main__':
    unittest.main()