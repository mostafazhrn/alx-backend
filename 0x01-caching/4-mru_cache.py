#!/usr/bin/python3
""" THis script shall create basic_cache that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ This instance of BasicCache inherits from BaseCaching """

    def __init__(self):
        """ This method sets the variable """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ This method assign item value to the key in self.cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                del_ky = self.keys.pop(-2)
                del self.cache_data[del_ky]
                print("DISCARD: {:s}".format(del_ky))

    def get(self, key):
        """ This method returns the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
