"""
https://leetcode.com/problems/odd-even-linked-list/
"""
from node.node_list import ListNode
class Solution:
    """
    The problem constraints the nodes to be odd->even->odd->even.

    So simply use two pointers and merge the odd and even list together.
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Start odd at first index and even at second index
        # evenHead gives a reference to the head of the even list.
        if not head:
            return None

        odd = head
        evenHead = even = head.next

        # Segregate odd and even lists
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Combine odd and even lists
        odd.next = evenHead

        return head


if __name__ == '__main__':
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    # n4 = ListNode(5)
    # n5 = ListNode(6)

    head.next = n1
    head.next.next = n2
    head.next.next.next = n3
    # head.next.next.next.next = n4
    # head.next.next.next.next.next = n5

    print("Before:")
    head.print_list(head)

    print("\n")

    new_head = Solution().oddEvenList(head)

    print("\nAfter:")
    new_head.print_list(new_head)