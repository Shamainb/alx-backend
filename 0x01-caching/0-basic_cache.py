#!/usr/bin/env python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BaseCaching:
    """
    BaseCaching class that defines the basic structure for a caching system.

    Attributes:
        cache_data (dict): A dictionary to store cached data.
    """

    def __init__(self):
        """
        Initializes the BaseCaching class with an empty cache_data dictionary.
        """
        self.cache_data = {}


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    and provides a basic caching system.
    This caching system does not impose any
    limit on the number of items in the cache.

    Methods:
        put(key, item):
            Adds an item to the cache with the specified key.
            If the key or item is None, this method does nothing.

        get(key):
        Retrieves the item associated with the given key from the cache.
        If the key is None or does not exist, returns None.
    """

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        Args:
            key (str): The key for the item.
            item (any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item associated with the given key from the cache.

        Args:
            key (str): The key for the item.

        Returns:
            The value associated with the key if it exists, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
