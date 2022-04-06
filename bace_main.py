import requests
from bs4 import BeautifulSoup
import re
from heapq import merge
from collections import Counter

HABRURL = 'https://habr.com/ru/post/547472/'
HABRTAG = {'title', 'span', 'p'}


class ClientWeb:
    soup = None

    def __init__(self, url, **keyword):
        #print('ClientWeb init ')
        self.url = url
        self.response = requests.get(self.url, **keyword)

    def __is_error__(self):
        #print('ClientWeb is_error')
        if self.response.status_code != 200:
            return Exception('Error 200')
        else:
            return True

    def get_date(self):
        if self.__is_error__():
            self.soup = BeautifulSoup(self.response.text, features='html.parser')
            return self.soup


class TextHandler:
    date = None
    tag = None
    quotes = None
    text = list()
    text_lower = None
    words = list()
    lang = 1

    def __init__(self, date, *tag):
        #print('TextHandler init')
        self.date = date
        self.tag = tag

    def __is_soup(self):
        if self.date == '':
            return Exception('Soup Empty')
        if self.date:
            return Exception('Soup None')
        else:
            return True

    def __is_tag(self):
        if self.tag == None:
            return Exception('Tag None')
        else:
            return True

    def __text_handler(self):
        #print('TextHandler __text_handler')
        if self.__is_soup():
            if self.__is_tag():
                self.quotes = self.date.find_all(self.tag)

    def __get_text(self):
        #print('TextHandler __get_text')
        self.__text_handler()
        for quote in self.quotes:
            self.text.append(quote.text.strip())

    def __text_lower(self):
        #print('TextHandler __text_lower')
        self.__get_text()
        self.text_lower = str(self.text).lower()

    def get_words(self):
        self.__text_lower()
        #print(self.lang)
        if self.lang == 1:
            self.words = list(merge(re.findall(r'\b[a-z]{3,15}\b', self.text_lower),
                                    re.findall(r'\b[а-я]{3,15}\b', self.text_lower)))
        elif self.lang == 2:
            self.words = list(re.findall(r'\b[a-z]{3,15}\b', self.text_lower))
        elif self.lang == 3:
            self.words = list(re.findall(r'\b[а-я]{3,15}\b', self.text_lower))
        return self.words

    def set_lang(self, lang):
        if lang in range(1, 3):
            self.lang = lang
        else:
            print('incorrect language')
            return Exception('incorrect language')


class Frequency:
    frequency = {}
    words = None
    top_n = None

    def __init__(self, words):
        #print('Frequency init')
        self.words = words

    def __frequency_counter(self):
        #print('Frequency count')
        self.frequency = Counter(self.words)
        self.num = len(self.frequency)
        self.frequency = dict(self.frequency)

    def get_frequency(self, num):
        self.__frequency_counter()
        self.top_n = Counter.most_common(self.frequency, num)
        self.top_n = dict(self.top_n)

    def print(self):
        for key in self.top_n.keys():
            print(key, self.top_n.get(key))


def main():
    date = ClientWeb(HABRURL)
    text = TextHandler(date.get_date(), HABRTAG)
    #text.set_lang(1)                            #установка языка не обязательно
    freq = Frequency(text.get_words())
    freq.get_frequency(3)
    freq.print()


if __name__ == '__main__':
    main()
