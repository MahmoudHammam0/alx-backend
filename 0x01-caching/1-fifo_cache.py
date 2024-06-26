#!/usr/bin/env python3
""" FIFO caching module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ inherits from BaseCaching """
    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(list(self.cache_data.keys())[0]))
            self.cache_data.pop(list(self.cache_data.keys())[0])

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
