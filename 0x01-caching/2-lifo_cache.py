#!/usr/bin/env python3
"""the `2-lifo_cache` module
defines the class `LIFOCache`
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """implements a caching system based on lifo cache replacement policy"""

    last_accessed = ''

    def put(self, key, item):
        """stores item in the cache and
        uses fifo algorithm to replace item when limit is reached"""

        if key and item:
            if not self.cache_data.get(key):
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print('DISCARD: {}'.format(LIFOCache.last_accessed))
                    del self.cache_data[LIFOCache.last_accessed]

            self.cache_data[key] = item
            LIFOCache.last_accessed = key

    def get(self, key):
        """retrieves items from the cache based on key, if it exists"""
        return self.cache_data.get(key)
