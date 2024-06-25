#!/usr/bin/python3
""" THis script shall create basic_cache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ This instance of BasicCache inherits from BaseCaching """

    def put(self, key, item):
        """ This method assigns the item value to key in self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ This method returns the value in self.cache_data linked to key """
        if key is None or key in self.cache_data:
            return self.cache_data[key]
        return None
