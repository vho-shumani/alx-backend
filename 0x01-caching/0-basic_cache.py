#!/usr/bin/env python3
"""BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class adds and retrieves data from dictionary
    """
    def __init__(self):
        """intializes variables"""
        super().__init__()

    def put(self, key, item):
        """Adds a new item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item from cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
