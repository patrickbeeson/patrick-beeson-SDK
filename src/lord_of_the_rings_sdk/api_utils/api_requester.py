import requests


class APIRequester:
    """
    Class to handle GET request via the requests library to a given
    API URL with assigned headers

    Attributes
    ---------
    url : string
        Complete URL used to access the API
    headers : dict
        Dictionary of any headers needed for the API request.
    """

    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.headers = kwargs.get('headers')
    
    def get(self):
        response = requests.get(
                self.url,
                headers=self.headers,
            )
        return response