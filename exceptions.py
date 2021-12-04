class BaseException(Exception):
    """
    базовый рейз
    :param args:
    :param kwargs:
    """
    message = 'урл не валидный'

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get('message', self.message)

class NotContainGz(BaseException):
    """
    рейз в случаев не гз составляющей
    """
    message = 'архив не tar.gz формата'

class UrlIsNotValid(BaseException):
    """
    рейз в случаев не гз составляющей
    """
    message = 'урл не валидный'
