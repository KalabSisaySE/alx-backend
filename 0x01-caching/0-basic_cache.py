#!/usr/bin/env python3
"""the `0-basic_cache` module
defines the class `BasicCache`
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """a basic caching system class"""

    def __init__(self) -> None:
        """instantiates a new `BasicCache` object"""
        super().__init__()

    def put(self, key, item):
        """puts an item in the storage"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value from storage linked to `key`"""
        return self.cache_data.get(key)
