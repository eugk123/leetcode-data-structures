"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
from node_list import ListNode
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

if __name__ == "__main__":

    node = ListNode(1)
    node.next = ListNode(2)

    print(node.val)