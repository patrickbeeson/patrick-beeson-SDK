import unittest
import requests_mock
from api_utils.api_requester import APIRequester


class TestAPIRequester(unittest.TestCase):

    def setUp(self):
        self.kwargs = {
            'url': 'https://example.com',
            'headers': {'Content-Type': 'application/json'},
        }
        self.requester = APIRequester(**self.kwargs)

    @requests_mock.Mocker()
    def test_api_requester_get_request(self, m):
        m.get('https://example.com', text='resp')
        self.assertEqual(
            self.requester.get().text,
            'resp'
        )


if __name__ == '__main__':
    unittest.main()