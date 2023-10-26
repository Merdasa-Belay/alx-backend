#!/usr/bin/env python3
""" fifo cach module """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching using FIFO """

    def __init__(self):
        """ construct class """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assign caching key to the item listed """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.queue.append(key)
            else:
                self.cache_data[key] = item
                discard = self.queue[0]
                del self.cache_data[self.queue[0]], self.queue[0]
                self.queue.append(key)
                print(f'DISCARD: {discard}')

    def get(self, key):
        """ get the item attached with a key """
        if key:
            return self.cache_data.get(key, None)
