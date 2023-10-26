#!/usr/bin/env python3
""" lifo cach module """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching using LIFO """

    def __init__(self):
        """ construct class """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ assign caching key to the item listed """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) <= self.MAX_ITEMS:
                pass
            else:
                del self.cache_data[self.last_key]
                print(f'DISCARD: {self.last_key}')
            self.last_key = key

    def get(self, key):
        """ get the item attached with a key """
        if key:
            return self.cache_data.get(key, None)
