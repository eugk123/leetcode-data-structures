"""
https://leetcode.com/problems/lru-cache/
"""
from collections import OrderedDict
class LRUCache(OrderedDict):
    """
    Linked Hash Map (OrderedDict) maintains the order of keys and values while typical Hash Map (Dict) doesn't.
    There is a structure called ordered dictionary (Linked Hash Map - combines behind both hashmap and linked list).
    Leveraging this data structure makes this problem easy.

    The trick is during the get operation, we want to move the item to the end. During the put operation, when exceeding
    capacity, we want to remove the first item.

    Understand this data structure in terms of space and complexity:
    - How is it constant time? It is a hash map. With the collection of hash codes and hash function disperses elements
    properly among the buckets.
    - What is the space? O(capacity)
    - How is it perserving order? It maintains a linked list of the entries in the map, in the order in which they were
    inserted.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        int get(int key) Return the value of the key if the key exists, otherwise return -1.

        To evict the least recently used key, need to reorder most recently used to the end.
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        # print(self)  # Check to see that the MRU was moved to the end.
        return self[key]

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key. (pop first entry)
        """
        self[key] = value
        # print(self)  # Check to see the LRU is indeed popped!
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last = False)
            # print("POPPING")
            # print(self)  # Check to see the LRU is indeed popped!

if __name__ == '__main__':
    obj = LRUCache(3)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.put(3, 3)
    print(obj.get(1))
    obj.put(4, 3)

