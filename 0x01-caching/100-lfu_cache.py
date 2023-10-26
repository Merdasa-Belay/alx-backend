#!/usr/bin/env python3
""" LFU cach module """


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching algorithm """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.queue = []

    @staticmethod
    def getDictionaryValue(dict_i):
        """ return the value of a key """
        dict_key = list(dict_i.keys())[0]
        return dict_i[dict_key]

    def put(self, key, item):
        """ assign caching key to the item listed """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.queue.append({key: 0})
            else:
                self.queue.sort(reverse=True,
                                key=self.getDictionaryValue)
                popped = self.queue.pop()
                dict_key = list(popped.keys())[0]
                del self.cache_data[dict_key]
                print("DISCARD: " + str(dict_key))

    def get(self, key):
        """ get the item attached with a key """
        if key in self.cache_data:
            i = 0
            for items in self.queue:
                key_it = list(items.keys())
                if key_it[0] == key:
                    newElement = {key: items[key_it[0]] + 1}
                    self.queue[i] = newElement
                i += 1
            return self.cache_data.get(key, None)
