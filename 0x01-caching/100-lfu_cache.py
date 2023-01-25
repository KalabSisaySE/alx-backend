#!/usr/bin/env python3
"""the `100-lfu_cache` module
defines the class `LFUCache`
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """implements a caching system using the LFU cache replacement policy"""

    def __init__(self) -> None:
        """instantiates a new LFUCache object"""
        super().__init__()
        self.recent_access = []
        self.access_count = {}

    def put(self, key, item):
        """stores item in the cache, if cache size reaches limit
        the least frequently used item will be replaced
        """
        if key and item:
            # if key is new is new for the cache
            if not self.cache_data.get(key):
                # if cache is full
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_frequency = min(self.access_count.values())
                    keys = [
                        key
                        for key, item in self.access_count.items()
                        if item == least_frequency
                    ]
                    if len(keys) > 1:
                        """two or more items having equal frequency"""
                        least_freq_recent = min(
                            # the least recent item will have a smaller index
                            {
                                key: self.recent_access.index(key)
                                for key in keys
                            }
                        )
                    else:
                        least_freq_recent = keys[0]
                    print("DISCARD: {}".format(least_freq_recent))
                    del self.cache_data[least_freq_recent]
                    del self.access_count[least_freq_recent]
                    self.recent_access.remove(least_freq_recent)

            self.cache_data[key] = item
            self.update_metadata(key)

    def get(self, key):
        """retrieves items from the cache based on key, if it exists"""
        self.update_metadata(key=key)
        return self.cache_data.get(key)

    def update_metadata(self, key):
        """updates access information after every
        put,update or get operation"""
        # only if key is in cache update its metadata
        if key in self.cache_data:
            if self.access_count.get(key):
                self.access_count[key] = self.access_count[key] + 1
            else:
                self.access_count[key] = 1
            if key in self.recent_access:
                self.recent_access.remove(key)
            self.recent_access.append(key)
