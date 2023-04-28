from lord_of_the_rings_sdk.api_utils.Abstract.content_type import ContentType


class Quote(ContentType):
    """
    Class representing a Quote content type.

    Attributes
    ----------
    lotr_sdk : function
    content_type : string
    """

    def __init__(self, lotr_sdk, content_type, **kwargs):
        super(Quote, self).__init__(lotr_sdk)
        self.lotr_sdk = lotr_sdk
        self.content_type = content_type
