class IncorrectURL(Exception):
    """Return exception if link is incorrect"""

    def __init__(self, *args):
        if args:
            self.error_message = args[0]
        else:
            self.error_message = None

    def __str__(self):
        if self.error_message:
            return f'Incorrect URL: {self.error_message}'
        else:
            return f'Incorrect URL'


class InvalidToken(Exception):
    """Return exception if API-Token is invalid"""

    def __str__(self):
        return 'Token is invalid'


class NotFindLink(Exception):
    """Return exception if link is not find"""

    def __init__(self, *args):
        if args:
            self.error_message = args[0]
        else:
            self.error_message = None

    def __str__(self):
        if self.error_message:
            return f'Not find URL: {self.error_message}'
        else:
            return f'Not find URL'
