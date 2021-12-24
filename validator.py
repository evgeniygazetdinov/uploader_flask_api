import validators
from exceptions import UrlIsNotValid


class UrlValidator:
    """
    проверяет урлу, и чекает tar.gz
    """

    def __init__(self, url_for_validate: str):
        self.url = url_for_validate
        self.check_url()

    def is_url(self):
        """
        чек
        урла это урла
        :return:
        """
        if not validators.url(self.url):
            raise UrlIsNotValid

    def check_url(self):
        """
        проверка урлы на параметры
        :return:
        """
        self.is_url()
        self.is_gz_extension()
