"""
https://leetcode.com/problems/add-binary/
"""
import collections
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Two ways to store the list:
        # 1) Doubly Linked List
        curr = head = ListNode(0)
        prev = None
        # 2) Queue
        queue = collections.deque([])
        
        if len(a) >= len(b):
            long = a
            short = b
        else:
            long = b
            short = a
            
        carry = 0
                    
        # read longer string in reverse
        for i in reversed(range(len(long))):
            
            # index for shorter string
            j = i - (len(long)-len(short))
            
            # Total the binary numbers
            # Eventually the shorter string will end, that's when we only add the longer digit
            if j >= 0:
                total = int(long[i]) + int(short[j]) + carry
            
            else:
                total = int(long[i]) + carry
            
            if total == 0:
                digit = '0'
                carry = 0
            elif total == 1:
                digit = '1'
                carry = 0
            elif total == 2:
                digit = '0'
                carry = 1
            elif total == 3:
                digit = '1'
                carry = 1
            
            # Doubly Linked List Traversal
            curr.next = ListNode(digit)  # Point to next with new node
            prev = curr  # Update prev
            curr = curr.next  # Traverse to next
            curr.prev = prev  # Point to previous

            # Queue Traversal
            queue.appendleft(digit)
        
        # Check if final digit has a carry.
        if carry == 1:
            # Doubly Linked List Traversal
            curr.next = ListNode('1')
            prev = curr  # Update prev
            curr = curr.next  # Traverse to next
            curr.prev = prev  # Point to previous

            # Queue Traversal
            queue.appendleft('1')
        
        # Doubly Linked List to result
        # We check for curr.prev is set to null because we started with head at ListNode(0) which needs to be skipped
        result = ""
        while curr.prev:            
            result = result + str(curr.val)
            curr = curr.prev
            
        # Queue to result
        # result = "".join(queue)
        return result