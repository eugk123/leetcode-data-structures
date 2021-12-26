class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):
    """
    Part I: Design HashMap with put, get, and remove operations. It should be error proof (challenge the interviewee to come up with something here).
    
    Optimal -> Closed Addressing / Chaining | LinkedList w/ Hashing demonstrating understanding of data structure -> Init, O(1) time and O(1) space
    Why O(1) space? This is because we can have a smaller size as oppose to using an array only solution! LinkedList will handle collisions.

    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000 
        self.hash_table = [None] * self.size  # O(1000) time and O(1000) space
        
    def put(self, key, value):
        index = key % self.size 

        curr = self.hash_table[index]

        if curr == None:
            # We do not have anything in this bin, just create a new node 
            self.hash_table[index] = ListNode(key,value)
        else:
            # Traverse until key is matching or none is found
            while True:

                # if key is matching, update value then return
                if curr.key == key:
                    curr.value = value
                    return
                
                # if none is found, point curr.next to new node
                if curr.next == None:
                    curr.next = ListNode(key,value)
                    return

                curr = curr.next

    def get(self, key):
        index = key % self.size 
        
        # Go to bin
        curr = self.hash_table[index]
        
        # Traverse linked list until key is found
        while curr:
            if curr.key == key:
                return curr.value 
            else:
                curr = curr.next
        
        # Otherwise return -1
        return -1
        

    def remove(self, key):
        index = key % self.size 
        
        # Go to bin, but store both curr and prev pointers to support removal
        curr = prev = self.hash_table[index]
        
        # Removing from empty bin just return
        if not curr: return 
        
        if curr.key == key:
            # If first node has matching key, remove by pointing to the 2nd node
            self.hash_table[index] = curr.next
        else:
            # We did not find the node to delete we must now traverse the bin
            curr = curr.next
            
            while curr:
                if curr.key == key:
                    # If found, remove curr!
                    prev.next = curr.next 
                    break
                else:
                    # Traverse pointers
                    prev, curr = prev.next, curr.next

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
