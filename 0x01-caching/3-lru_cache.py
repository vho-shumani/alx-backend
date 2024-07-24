#!/usr/bin/env python3
""" 3-lru_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Adds and retrieve data from dictionary
    using LRU algorithm
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
                    self.cache_data.pop(self.ordered_list[0])
                    print(f"DISCARD: {self.ordered_list[0]}")
                    self.ordered_list.pop(0)
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
