from collections import OrderedDict


class LRUCache(object):
    # An oldest element put/access in the queue is the Least Recently Used one.
    # In this data structure, the LRU is the first element in the queue.
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()  # Keep the key in the insersion order.

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # Reorder the dictionary
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)  # Get rid of the old value of the existed key.
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)  # FIFO if last is set to False.
        self.cache[key] = value


if __name__ == '__main__':
    capacity = 2
    cache = LRUCache(capacity)
    cache.set(2, 1)
    print cache.cache

    cache.set(1, 1)
    print cache.cache

    cache.set(2, 3)
    print cache.cache

    cache.set(4, 1)
    print cache.cache

    print cache.get(1)
    print cache.cache

    print cache.get(2)
    print cache.cache

