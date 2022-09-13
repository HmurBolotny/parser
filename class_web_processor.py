import requests
from bs4 import BeautifulSoup


class ClientWeb:
    soup = None

    def __init__(self, url, **keyword):
        #print('ClientWeb init ')
        self.url = url
        try:
            self.response = requests.get(self.url, **keyword)
            print(self.response.content)
            self.connect = True
        except requests.ConnectionError:
            print('error url')
            self.response = None
            Exception('error url')

    def __is_error__(self):
        if self.response is None:
            return False
        if self.response.status_code == 200:
            return True
        else:
            #return Exception('Error 200')
            return False

    def get_date(self):
        if self.__is_error__():
            self.soup = BeautifulSoup(self.response.text, features='html.parser')
            return self.soup
