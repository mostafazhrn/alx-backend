#!/usr/bin/python3
""" THis script shall create basic_cache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ This instance of BasicCache inherits from BaseCaching """

    def __init__(self):
        """ This method sets the variable """
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """ This method assign item value to the key in self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 1
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                del_key = self.keys.pop(0)
                del self.cache_data[del_key]
                del self.count[del_key]
                print("DISCARD: {:s}".format(del_key))

    def get(self, key):
        """ This method returns the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            self.count[key] += 1
            return self.cache_data[key]
        return None
