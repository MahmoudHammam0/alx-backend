#!/usr/bin/env python3
""" Basic dictionary module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching """
    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
