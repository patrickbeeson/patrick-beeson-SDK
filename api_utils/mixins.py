import json
from urllib.parse import urlencode


def create_params(**kwargs):
    '''
    '''
    url = kwargs.get('url')
    params = kwargs.get('params')
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'

class PathBuilder:
    '''
    Used to build the correct API path that includes
    parameters & filters
    '''
    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.version = kwargs.get('version')
        self.content_type = kwargs.get('content_type')
        self.id = kwargs.get('id')
        self.extra = kwargs.get('extra')
        self.params = kwargs.get('params')
        
    def build(self):
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