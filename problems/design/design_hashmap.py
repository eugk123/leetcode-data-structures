"""
https://leetcode.com/problems/design-hashmap
"""
class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class HashMap:
    """
    Chaining - uses linked lists at every bucket to avoid collisions.

    Time Complexity: O(n) worst case puts, gets, removes, when all key,value pairs happen to be placed in the same bucket

    In comparison to Open Addressing / Linear Probing
    Cons: Not uniformly distributed when compared with Open Addressing
    Pros: Handles collisions using linked list - does not need to rehash with Load Factor
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000    # Initial size can be anything. Just pick a large enough number
        self.hash_map = self.size * [None]        # Initialize with empty objects
        return

    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size     # Simple hash function to guarantee placement in the array
        
        current = self.hash_map[index]

        # First check if there is a ListNode at current index
        if current == None:
            print("PUT key:{} has been created with val:{}, located at index:{}, new listnode".format(key,val,index))
            self.hash_map[index] = ListNode(key, val)
            return

        # Otherwise, iterate through existing listnode, until key is found, then update
        node_number = 0
        while current:
            # If key found, update value then return
            if key == current.key:
                current.val = val
                print("PUT key:{} has been updated with val:{}, located at index:{}, with node number:{}".format(key,val,index,node_number))
                return
            prev = current
            current = current.next
            node_number += 1

        # If no key was found, then append to end
        print("PUT key:{} has been created with val:{}, located at index:{}, appended to end with node number:{}".format(key,val,index,node_number))
        prev.next = ListNode(key, val)
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size

        # Search for key in ListNode on the calculated index.
        current = self.hash_map[index]
        node_number = 0
        
        while current:
            # If key found, update value then return
            if key == current.key:
                print("GET key:{} has been found, returning val:{}, located at index:{}, with node_number:{}".format(key,current.val,index,node_number))
                return current.val
            current = current.next
            node_number += 1
        
        print("GET key:{} has no value".format(key))
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size

        current = self.hash_map[index]
        prev = None
        node_number = 0
        while current:
            if key == current.key:                
                # If key was found at first ListNode, we set to the next
                if prev == None:
                    print("REMOVE key:{} has been found, located at index:{}, with node_number:{}".format(key,index,node_number))
                    self.hash_map[index] = current.next
                
                else:
                    # If key was found between two ListNodes, we'll have to skip the current node by setting prev.next
                    # If key was found at end, the same logic can be applied since current.next in this case will be None
                    print("REMOVE key:{} has been found, located at index:{}, with node_number:{}".format(key,index,node_number))
                    prev.next = current.next
  
                return

            prev = current
            current = current.next
            node_number += 1

        # If end is reached, and no key was found, then do nothing 
        print("REMOVE key:{} has not been found.".format(key))
        return

if __name__ == '__main__':
    key_to_value = HashMap()
    key_to_value.put(1, 1)
    key_to_value.put(1001, 2)
    key_to_value.put(2001, 3)
    key_to_value.put(3001, 4)
    key_to_value.put(4001, 5)

    key_to_value.get(1)
    key_to_value.get(1001)
    key_to_value.get(2001)

    key_to_value.remove(1001)   # 1->1001->2001->3001->4001, 1001 is at node_number 1
    key_to_value.remove(2001)   # 1->2001->3001->4001, 2001 is at node_number 1
    key_to_value.remove(1)      # 1->3001->4001, 1 is at node_number 0
    key_to_value.remove(4001)   # 3001->4001, 4001 is at node_number 1

    