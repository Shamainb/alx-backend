#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a
    Last-In-First-Out (LIFO) caching system.

    This class inherits from BaseCaching and
    overrides the put and get methods
    to handle LIFO caching. When the cache
    exceeds MAX_ITEMS, the most recently
    added item is discarded.

    Attributes:
        None additional to those inherited from BaseCaching.
    """
    
    def __init__(self):
        """
        Initializes the LIFOCache class, calling
        the parent class's __init__ method
        to set up the cache_data dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache. If the
        cache exceeds MAX_ITEMS, it discards
        the most recently added item based on the LIFO algorithm.

        Args:
            key (str): The key for the item.
            item (any): The value to be stored in the cache.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # Remove the key if it already exists to update its position
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently added item (LIFO)
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Add the new item to the cache
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
