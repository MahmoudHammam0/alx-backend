#!/usr/bin/env python3
""" LRU Caching module """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ inherits from BaseCaching """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.record = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.record:
            self.record.remove(key)
        self.record.append(key)
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.record[0]))
            self.cache_data.pop(self.record[0])
            self.record.pop(0)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.record:
            self.record.remove(key)
            self.record.append(key)
        return self.cache_data[key]
