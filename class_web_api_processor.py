import requests


class WebParserApi:
    url = None
    response = None
    data = None

    def __init__(self, url, **keyword):
        self.url = url

    def get_requests(self, *arg):
        try:
            self.response = requests.get(self.url, *arg)
        except requests.ConnectionError as exc:
            print(exc)

    def __is_error__(self):
        if self.response is None:
            return False
        if self.response.status_code == 200:
            return True

    def get_data(self):
        if self.__is_error__():
            self.data = self.response.content.decode()
            return self.data

    def print(self):
        print(self.data)
        print('\n')
        print(self.response.content)
