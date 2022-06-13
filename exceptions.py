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
