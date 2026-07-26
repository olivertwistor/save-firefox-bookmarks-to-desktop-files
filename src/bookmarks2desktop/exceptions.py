"""
Definitions of custom exceptions and errors.
"""


class InvalidBookmarksDictError(Exception):
    """
    Raises when a dict isn't from a valid Firefox bookmarks file.
    """
    def __init__(self, message: str, *args):
        self.message = message
        super(InvalidBookmarksDictError, self).__init__(message, *args)
