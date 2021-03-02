"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            # head = []
            if not head:
                return None

            # head = [1]
            if head and not head.next:
                return head

            first_node = head
            second_node = head.next

            first_node.next = helper(head.next.next)
            second_node.next = first_node

        return helper(head)