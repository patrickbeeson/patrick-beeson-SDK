import requests

class APIRequester:
    '''
    '''
    def __init__(self, **kwargs):
        self.url = kwargs.get('url')
        self.headers = kwargs.get('headers')
    
    def get(self):
        response = requests.get(
                self.url,
                headers=self.headers,
            )
        return response