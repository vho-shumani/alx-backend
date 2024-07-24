#!/usr/bin/env python3
""" 1-fifo_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Adds and retrieve data from dictionary
    using FIFO algorithm
    """
    def __init__(self):
        """Initializes variables"""
        super().__init__()

    def put(self, key, item):
        """Add a new item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard_key = next(iter(self.cache_data))
                    self.cache_data.pop(discard_key)
                    print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves item from cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
