from collections import Counter


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
