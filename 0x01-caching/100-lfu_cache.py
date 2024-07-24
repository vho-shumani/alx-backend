#!/usr/bin/env python3
""" 4-mru_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Adds and retrieve data from dictionary
    using MRU algorithm
    """
    def __init__(self):
        """Initializes variables"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Add a new item in the cache
        """
        if key and item:
            counter = 0
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    key_discard = self.lfu_key()
                    self.cache_data.pop(key_discard)
                    self.frequency.pop(key_discard)
                    print(f"DISCARD: {key_discard}")
                else:
                    counter = self.frequency[key] + 1
                    del self.cache_data[key]
            self.cache_data[key] = item
            self.frequency[key] = counter

    def get(self, key):
        """ Retrieves item from cache
        """
        if not key or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data[key]

    def lfu_key(self):
        """Retrieves the least frequently used key.
        """
        for key in self.frequency.keys():
            if self.frequency[key] == min(self.frequency.values()):
                return key
