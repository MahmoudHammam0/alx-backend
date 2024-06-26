#!/usr/bin/env python3
""" LFU Caching module """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ inherits from BaseCaching """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.record = []
        self.freq = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            freq_list = list(self.freq.items())
            freqs = [freq[1] for freq in freq_list]
            minimum = min(freqs)
            lfu = [freq[0] for freq in freq_list if freq[1] == minimum]
            for k in self.record:
                if k in lfu:
                    lf_key = self.record.pop(self.record.index(k))
                    self.cache_data.pop(k)
                    self.freq.pop(k)
                    print("DISCARD: {}".format(k))
        if key in self.record:
            self.record.remove(key)
            self.record.append(key)
            self.freq[key] += 1
        else:
            self.record.append(key)
            self.freq[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.record:
            self.record.remove(key)
            self.record.append(key)
            self.freq[key] += 1
        return self.cache_data[key]
