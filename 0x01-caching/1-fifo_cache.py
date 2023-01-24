#!/usr/bin/env python3
"""the `1-fifo_cache` module
defines the class `FIFOCache`
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """a cahcing system based on the fifo cache replacement policy"""

    def put(self, key, item):
        """puts item in the cahce
        and uses fifo algorithm to replace item when limit is reached"""
        if key and item:
            # if key is new for cache storage
            if not self.cache_data.get(key):
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first = list(self.cache_data.keys())[0]
                    print("DISCARD: {}".format(first))
                    del self.cache_data[first]

            self.cache_data[key] = item

    def get(self, key):
        """return the value from storage linked to `key` if key exists"""
        return self.cache_data.get(key)
