"""
https://leetcode.com/problems/linked-list-cycle-ii
"""
from node.node_list import ListNode
class Solution:
    """
    Simply use a HashSet. Add to set if not seen. Otherwise, return curr
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        nodesSeen = set()

        curr = head
        while curr:
            if curr not in nodesSeen:
                nodesSeen.add(curr)
            else:
                return curr
            curr = curr.next

        return None