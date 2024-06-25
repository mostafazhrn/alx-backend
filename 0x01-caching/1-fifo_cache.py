#!/usr/bin/python3
""" THis script shall create basic_cache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ This instance shall rep that BasicCache inherits from BaseCaching """

    def __init__(self):
        """ This method sets the variable """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ This method shall assigns item value self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)
        if len(self.keys) > BaseCaching.MAX_ITEMS:
            del_key = self.keys.pop(0)
            del self.cache_data[del_key]
            print("DISCARD: {:s}".format(del_key))

    def get(self, key):
        """ This method returns the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
