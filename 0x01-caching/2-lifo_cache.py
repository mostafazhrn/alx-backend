#!/usr/bin/python3
""" THis script shall create basic_cache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ This instance of BasicCache inherits from BaseCaching """

    def __init__(self):
        """ This method sets the variable """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ This method assigns the item value to the key in self.cache_data """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {:s}".format(self.last_key))
                del self.cache_data[self.last_key]
            self.last_key = key
    
    def get(self, key):
        """ This method returns the value in self.cache_data linked to key """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
