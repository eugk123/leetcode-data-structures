"""
https://leetcode.com/problems/linked-list-
"""
from node.node_list import ListNode
class Solution:
    """
    Two Pointer - Fast and Slow. Use try/except. Makes it so much easier.
    """
    def hasCycle(head):  # Two Pointer Solution
        slow = fast = head
        try:
            while slow:
                slow = slow.next
                fast = fast.next.next
                if slow.val == fast.val:
                    return True
        except:
            return False