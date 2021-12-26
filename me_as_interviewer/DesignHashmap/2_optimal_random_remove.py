import random
class MyHashMap(object):
    """
    https://leetcode.com/problems/design-hashmap/

    Part II: Design HashMap with a random key remove function. (hint: you need another data structure for removal)

    Rule:
    1. Must use a data structure whose size will change when a key is removed. This can be a dictionary.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_value = {}
        self.index_to_key = {}  # supports random remove
        self.key_to_index = {}  # supports simple remove with the addition of random remove

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.key_to_value[key] = value

        # With a new key, need to add it to the rest of the maps
        index = len(self.key_to_value) - 1
        self.index_to_key[index] = key
        self.key_to_index[key] = index

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.key_to_value:
            return self.key_to_value[key]
        else:
            return -1

    def remove_random(self):
        """
        Remove a random key

        HINT: You need two additional data structures to make this work.
        """
        random_index = random.randrange(0, len(self.key_to_value) - 1)
        random_key = self.index_to_key(random_index)
        self.key_to_value.pop(random_key)

        # Clean up other maps
        self.key_to_index.pop(random_key)
        self.index_to_key.pop(random_index)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.key_to_value:
            self.key_to_value.pop(key)

        # With a removal key, need to remove it to the rest of the maps
        index = self.key_to_index[key]  # Find value of index for particular key
        self.index_to_key.pop(index)
        self.key_to_index.pop(key)

if __name__ == '__main__':
    # Initialize
    obj = MyHashMap()

    # PUT for any key value pairs
    obj.put(4, 9)
    obj.put(1, 22)
    obj.put(3, 5)
    obj.put(2, 6)
    obj.put(8, 15)
    obj.put(0, 3)
    obj.put(9, 14)

    # GET for valid key returns value
    print("GET for valid key {} returns value: {}".format(2, obj.get(2)))
    print("GET for valid key {} returns value: {}".format(3, obj.get(3)))

    # GET for invalid key returns -1
    print("GET for invalid key {} returns -1: {}".format(10, obj.get(10)))

    # RANDOM REMOVE for valid key 
    print("REMOVE for valid key, reduces length of map by one")

    # REMOVE for valid key 
    print("REMOVE for valid key, reduces length of map by one")
    print("Current length of map: {}".format(len(obj.key_to_value)))
    obj.remove(2)
    print("Current length of map: {}".format(len(obj.key_to_value)))

    # REMOVE for invalid key
    print("REMOVE for invalid key, does not reduce length of map")
    obj.remove(2)
    print("Current length of map: {}".format(len(obj.key_to_value)))

    # After all these removes, we want to prove that the random remove is still working!``