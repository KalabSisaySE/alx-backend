#!/usr/bin/env python3
"""the `4-mru_cache` module
defines the class `MRUCache`
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """implements a caching system based on MRU cache replacement policy"""

    def __init__(self) -> None:
        """instantiates a new MRUCaching object"""
        super().__init__()
        self.recent_access = []

    def put(self, key, item):
        """stores items in the cache and
        if cache size reaches limit
        most recently used item will be replaced"""
        if key and item:
            # if item is new
            if not self.cache_data.get(key):
                # if limit reached
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    most_recent = self.recent_access[-1]
                    print("DISCARD: {}".format(most_recent))
                    del self.cache_data[most_recent]
                    self.recent_access.remove(most_recent)

            self.cache_data[key] = item
            # if item already exists remove it first
            # to avoid duplicates
            if key in self.recent_access:
                self.recent_access.remove(key)
            self.recent_access.append(key)

    def get(self, key):
        """retrieves items from the cache based on key, if it exists"""
        if key in list(self.cache_data.keys()):
            # update the recent access list
            if key in self.recent_access:
                self.recent_access.remove(key)
            self.recent_access.append(key)
        return self.cache_data.get(key)
