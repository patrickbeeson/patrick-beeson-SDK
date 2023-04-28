class ContentType(object):

    def __init__(self, lotr_sdk):
        self.lotr_sdk = lotr_sdk
    
    def get(self, params=None, headers=None, id=None, extra=None):
        return self.lotr_sdk.request(
            self.content_type,
            params=params,
            headers=headers,
            id=id,
            extra=extra
        )
