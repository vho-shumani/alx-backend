#!/usr/bin/env python3
""" 4-mru_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Adds and retrieve data from dictionary
    using MRU algorithm
    """
    def __init__(self):
        """Initializes variables"""
        super().__init__()
        self.ordered_list = []

    def put(self, key, item):
        """Add a new item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    key_discard = self.ordered_list[BaseCaching.MAX_ITEMS - 1]
                    self.cache_data.pop(key_discard)
                    print(f"DISCARD: {key_discard}")
                    self.ordered_list.pop()
                else:
                    self.ordered_list.remove(key)
                    del self.cache_data[key]
            self.cache_data[key] = item
            self.ordered_list.append(key)

    def get(self, key):
        """ Retrieves item from cache
        """
        if not key or key not in self.cache_data:
            return None
        self.ordered_list.remove(key)
        self.ordered_list.append(key)
        return self.cache_data[key]
