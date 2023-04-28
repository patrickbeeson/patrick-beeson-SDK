from dotenv import dotenv_values

from lord_of_the_rings_sdk.api_utils.api_requester import APIRequester
from lord_of_the_rings_sdk.api_utils.mixins import PathBuilder
from lord_of_the_rings_sdk.exceptions.api_exception import ApiException

config = dotenv_values(".env")


class Client(object):
    """
    Class representing the API client to handle the complete request. Provides
    access to the response as JSON as well as the status code.

    Attributes
    ----------
    base_url : string
    version : string
    _movie : property
        Method to instantiate the Movie object
    _quote : property
        Method to instantiate the Quote object
    """

    def __init__(self):
        self.base_url = config['LOTR_API_BASE_URL']
        self.version = config['LOTR_API_VERSION']

        # Supported content types
        self._movie = None
        self._quote = None


    def request(
            self,
            content_type,
            id=None,
            extra=None,
            params=None,
            headers=None
        ):

        headers = headers or {}
        headers['Authorization'] = config['LOTR_AUTH_BEARER_TOKEN']
        
        params = params or {}

        url = PathBuilder(
            base_url=self.base_url,
            version=self.version,
            content_type=content_type,
            id=id,
            extra=extra,
            params=params
        ).build()

        api = APIRequester(url=url, headers=headers)
        try:
            response = api.get()
        except:
            raise ApiException("There was a problem requesting the LOTR API.")
        json_response = response.json()

        return {
            'status': response.status_code,
            'json': json_response
        }

    @property
    def movie(self):
        if self._movie is None:
            from rest.movie import Movie
            self._movie = Movie(self, 'movie')
        return self._movie

    @property
    def quote(self):
        if self._quote is None:
            from rest.quote import Quote
            self._quote = Quote(self, 'quote')
        return self._quote