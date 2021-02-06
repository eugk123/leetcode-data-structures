"""
https://leetcode.com/problems/remove-linked-list-elements
"""
from node_list import ListNode
class Solution:
    """
    Two pointer.

    O(n) time and O(1) space
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = prev.next

        # Trim inbetween first duplicates and last
        while curr:
            if curr.val == val:
                curr = curr.next

                # In case last digit is  curr points to None, we need prev to point to None
                if not curr:
                    prev.next = None
                elif curr.val != val:
                    prev.next = curr
            elif curr.val != val:
                curr = curr.next
                prev = prev.next

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)

    head.next = n1
    head.next.next = n2
    head.next.next.next = n3
    head.next.next.next.next = n4

    print("Before:")
    head.print_list(head)

    print("\n")

    new_head = Solution().removeElements(head, val=1)

    print("\nAfter:")
    new_head.print_list(new_head)