#!/usr/bin/env python3
""" basic caching """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache is a class that perform
    basic caching data operation
    """

    def put(self, key, item):
        """ assign caching key to the item listed """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get the item attached with a key """
        if key:
            return self.cache_data.get(key, None)
