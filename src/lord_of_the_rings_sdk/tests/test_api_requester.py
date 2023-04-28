import unittest
import requests_mock
import json
from lord_of_the_rings_sdk.api_utils.api_requester import APIRequester


class TestAPIRequester(unittest.TestCase):

    def setUp(self):
        self.kwargs = {
            'url': 'https://example.com',
            'headers': {'Content-Type': 'application/json'},
        }
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
        self.requester = APIRequester(**self.kwargs)

    @requests_mock.Mocker()
    def test_api_requester_get_request(self, m):
        m.get(
            'https://example.com',
            json=self.mock_json_response
        )
        self.assertEqual(
            self.requester.get().status_code,
            200
        )
        self.assertEqual(
            self.requester.get().json(),
            self.mock_json_response
        )


if __name__ == '__main__':
    unittest.main()