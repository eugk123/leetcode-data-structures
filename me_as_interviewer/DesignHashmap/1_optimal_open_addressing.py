"""
Part I: Design HashMap with put, get, and remove operations. It should be error proof (challenge the interviewee to come up with something here).

Optimal -> Open Addressing w/ Linear Probing | Use array collection with arbituary large size. When collision occurs, perform linear scan to right to populate empty index. 

Due to interest of time, hash function can be as simple as: key % size
"""
class MyHashMap:
    def __init__(self):
        self.size = 1000003  # Prime number has better chance of less collisions
	                         # Could be made smaller, and do load balancing. (I'm too lazy)
        self.container = self.size * [None]

    def put(self, key: int, value: int) -> None:
        idx = self.get_index(key)
        self.container[idx] = (key, value)

    def get(self, key: int) -> int:
        item = self.container[self.get_index(key)]
        return item[1] if item is not None else -1

    def remove(self, key: int) -> None:
        self.container[self.get_index(key)] = None

    def get_index(self, key: int) -> bool:
        index = self.hasher(key)
        item = self.container[index]

        # Linear probe collision handling
        while item is not None:
            if item[0] == key:
                return index
            index += 1
            item = self.container[index]

        return index

    def hasher(self, key):
        # h = hashlib.sha256()
        # h.update(repr(key).encode())
        return key % self.size

if __name__ == '__main__':
    # Initialize
    obj = MyHashMap()

    # PUT for any key value pairs
    obj.put(0, 9)
    obj.put(4, 9)
    obj.put(1, 3)
    obj.put(3, 5)
    obj.put(2, 6)

    # GET for valid key returns value
    print("GET for valid key {} returns value: {}".format(0, obj.get(0)))
    print("GET for valid key {} returns value: {}".format(2, obj.get(2)))
    print("GET for valid key {} returns value: {}".format(3, obj.get(3)))
    print("GET for valid key {} returns value: {}".format(4, obj.get(4)))

    obj.put(2, 30)
    print("GET for valid key {} returns value: {}".format(2, obj.get(2)))

    # GET for invalid key returns -1
    print("GET for invalid key {} returns -1: {}".format(10, obj.get(10)))

    # REMOVE for valid key 
    print("REMOVE for valid key, should return -1 for that key once removed")
    obj.remove(2)
    print("GET for removed key {} returns -1: {}".format(2, obj.get(2)))

    # REMOVE for invalid key
    print("REMOVE for valid key, should return -1 for that key once removed")
    obj.remove(4)
    print("GET for removed key {} returns -1: {}".format(4, obj.get(4)))
