#!/usr/bin/env python3
"""the `3-lru_cache` module
defines the class `LRUCache`
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """implements a caching system based on the LRU cache replacement policy"""

    recent_access = []

    def put(self, key, item):
        """stores items in the cache and
        if cache size reaches limit
        least recently used item will be replaced"""
        if key and item:
            # if item is new
            if not self.cache_data.get(key):
                # if limit reached
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_recent = LRUCache.recent_access[0]
                    print("DISCARD: {}".format(least_recent))
                    del self.cache_data[least_recent]
                    LRUCache.recent_access.remove(least_recent)

            self.cache_data[key] = item
            # if item already exists remove it first
            # to avoid duplicates
            if key in LRUCache.recent_access:
                LRUCache.recent_access.remove(key)
            LRUCache.recent_access.append(key)

    def get(self, key):
        """retrieves items from the cache based on key, if it exists"""
        if key in list(self.cache_data.keys()):
            # update the recent access list
            if key in LRUCache.recent_access:
                LRUCache.recent_access.remove(key)
            LRUCache.recent_access.append(key)
        return self.cache_data.get(key)
