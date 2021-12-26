class MyHashMap(object):
    # Non-dictionary solution
    # The key hint is your array should be initialized with [-1] * some arbituary size!
    # Naive -> Array, less optimal than chaining due to having a large self.size and can result in keys going beyond the initial size.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000001 
        self.map = [-1] * self.size  # O(1000001) time and O(1000001) space
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key > self.size:   # O(1) time and O(1) space
            return
        self.map[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int  
        :rtype: int
        """
        return self.map[key]   # O(1) time and O(1) space

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key > self.size:   # O(1) time and O(1) space
            return
        self.map[key] = -1

if __name__ == '__main__':
    # Initialize
    obj = MyHashMap()

    # PUT for any key value pairs
    obj.put(4, 0)
    obj.put(1, 3)
    obj.put(3, 5)
    obj.put(2, 6)

    # GET for valid key returns value
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
