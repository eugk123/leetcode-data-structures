class MyHashMap(object):
    """
    https://leetcode.com/problems/design-hashmap/
    
    Design HashMap with put, get, and remove operations. It should be error proof (challenge the interviewee to come up with something here).
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_value = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.key_to_value[key] = value

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

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.key_to_value:
            self.key_to_value.pop(key)

if __name__ == '__main__':
    # Initialize
    obj = MyHashMap()

    # PUT for any key value pairs
    obj.put(4, 9)
    obj.put(1, 3)
    obj.put(3, 5)
    obj.put(2, 6)

    # GET for valid key returns value
    print("GET for valid key {} returns value: {}".format(2, obj.get(2)))
    print("GET for valid key {} returns value: {}".format(3, obj.get(3)))

    # GET for invalid key returns -1
    print("GET for invalid key {} returns -1: {}".format(10, obj.get(10)))

    # REMOVE for valid key 
    print("REMOVE for valid key, reduces length of map by one")
    print("Current length of map: {}".format(len(obj.key_to_value)))
    obj.remove(2)
    print("Current length of map: {}".format(len(obj.key_to_value)))

    # REMOVE for invalid key
    print("REMOVE for invalid key, does not reduce length of map")
    obj.remove(2)
    print("Current length of map: {}".format(len(obj.key_to_value)))