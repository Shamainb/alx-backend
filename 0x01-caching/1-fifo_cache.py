#!/usr/bin/env python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that implements a First-In-First-Out (FIFO)
    algorithm for cache eviction.

    Attributes:
        order (list): A list to keep track of the order
        of keys for FIFO eviction.
    """

    def __init__(self):
        """
        Initializes the FIFOCache class,
        calling the parent class's __init__ method
        and initializing an empty order list to manage FIFO order.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache. If the cache exceeds MAX_ITEMS, it discards
        the oldest item based on the FIFO algorithm.

        Args:
            key (str): The key for the item.
            item (any): The value associated with the key.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

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
