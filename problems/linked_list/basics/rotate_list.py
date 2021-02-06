"""
https://leetcode.com/problems/rotate-list/
"""
from node_list import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        # Create cycle and set tail
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head

        # With the length, take modulus of k to find number of traversals
        n = k % length

        print(n, length, curr.val)

        # Traverse length - n + 1 times to the right. +1 because we need prev to be at the end and curr to be new head to break the cycle.
        # Set head, then break the cycle.
        # So if k is 2, traverse 3 + 1 times, set head on curr, then break cycle.
        count = 0
        prev = curr
        while curr and count < length - n:
            # print(prev.val)
            # Traverse curr
            curr = curr.next

            # Traverse prev
            prev = curr
            count += 1

        curr = curr.next

        # Break the circuit!
        prev.next = None
        return curr
