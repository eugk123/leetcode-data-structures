"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(val)
        self.next = next
        self.random = random

class Solution:
    """
    Hash Map (original -> copy)
    Time O(n)
    Space O(n)
    """
    def copyRandomList(self, head: Node) -> Node:
        # Edge case
        if not head:
            return head
        
        # To fully copy, we simply need to create a map that contains original node and copied node
        original_to_copy = {}
        
        # First pass - copy nodes with just the value
        curr = head
        while curr:
            original_to_copy[curr] = Node(curr.val)
            curr = curr.next
        
        
        # Second pass - set pointers
        curr = head
        while curr:
            copy = original_to_copy[curr]
            
            if curr.next:
                copy_next = original_to_copy[curr.next]
                copy.next = copy_next
            
            if curr.random:
                copy_random = original_to_copy[curr.random]
                copy.random = copy_random
            
            curr = curr.next
    

        return original_to_copy[head]