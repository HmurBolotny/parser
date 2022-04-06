import re
from heapq import merge


class TextHandler:
    date = None
    tag = False
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
        if self.tag:
            return True
        else:
            return Exception('Tag None')


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
