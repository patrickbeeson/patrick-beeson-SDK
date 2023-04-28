import json
from urllib.parse import urlencode


class PathBuilder:
    """
    Class to handle building complete API URL via the build method and
    instantiated attributes

    Attributes
    ----------
    base_url : str
        the base URL for the API
    version : str
        the version of the API used. ex. v2
    content_type : str
        the type of content being requested. ex. movie or quote
    id : string
        the unique identifier for an individual content type record
    extra: string
        additional path depth for a given API URL. ex. quote
    params: dict
        querystring params used to sort or filter the API. ex {limit: 1}

    Methods
    -------
    build
        Returns the complete API URL as a string
    """

    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.version = kwargs.get('version')
        self.content_type = kwargs.get('content_type')
        self.id = kwargs.get('id')
        self.extra = kwargs.get('extra')
        self.params = kwargs.get('params')
        
    def build(self):
        """
        Method handling actual URL construction. Currently supported
        content types are movies and quotes
        """
        paths = {
            'content_types': {
                'movie': {
                    'path': 'movie'
                },
                'quote': {
                    'path': 'quote'
                }
            }
        }
        content_type_info = paths['content_types'][self.content_type]
        sections = [content_type_info['path']]
        if self.id:
            sections.append(self.id)
        if self.extra:
            sections.append(self.extra)
        
        path = f'/{"/".join(sections)}'
        url = f'{self.base_url}/{self.version}{path}'
        
        params = {}
        for param in self.params.keys():
            params[param] = self.params[param]
        if params:
            url = create_params(params=json.dumps(params), url=url)

        return url


def create_params(**kwargs):
    """
    Function to construct querystring URL + querystring params, returned as
    a string
    """
    url = kwargs.get('url')
    params = kwargs.get('params')
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'