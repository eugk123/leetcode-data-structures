"""
https://leetcode.com/problems/lru-cache/
"""
class ListNode:
    # doubly linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    """
    Doubly Linked List with Hashmap

    Constant Time Put and Get operations.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node; key is the key that way we can get in constant time!

        # need dummy pointers. without them, we won't pass edge cases.
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        # connect the head and tail
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        """
        int get(int key) Return the value of the key if the key exists, otherwise return -1.

        To evict the least recently used key, need to reorder most recently used to the end.
        """
        if key not in self.cache:
            return -1
        else:
            # key exists, 
            # update node to head, since LRU
            curr = self.cache.get(key)
            self.removeNode(curr)
            self.insertNode(curr)
            return self.cache.get(key).value
     
    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key. (pop first entry)
        """
        #  h       t
        # (0) <-> (0)
        if key in self.cache:
            curr = self.cache.get(key)
            curr.value = value

            # update to head since LRU
            self.removeNode(key)
            self.insertNode(key)
        else:
            # new key to be added
            # full capacity, evict LRU at tail
            if len(self.cache) == self.capacity:
                # find the LRU at the tail.prev
                lru = self.tail.prev

                # remove LRU key and node
                self.cache.pop(lru.key)
                self.removeNode(lru)

            # insert key and node
            curr = ListNode(key, value)
            self.cache[key] = curr
            self.insertNode(curr)

    def insertNode(self, node: ListNode) -> None:
        """
        BEFORE                  AFTER
        head <-> head.next      prev <-> node <-> next
        prev     next
        """
        # attach
        p = self.head
        n = self.head.next

        p.next = n.prev = node
        node.prev, node.next = p, n


    def removeNode(self, node: ListNode) -> None:
        """
        BEFORE                          AFTER
        tail.prev <-> node <-> tail     prev <----------> next        
        prev                   next
        """
        # detach
        n = node.next
        p = node.prev

        # this will work with dummy pointers since dummy tail and head point to itself for it's init connection
        p.next, n.prev = n, p

if __name__ == '__main__':
    obj = LRUCache(3)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.put(3, 3)
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(3))
    obj.put(4, 3)
    print(obj.get(1))

