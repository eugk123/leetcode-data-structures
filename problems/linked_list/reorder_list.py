"""
https://leetcode.com/problems/reorder-list/
"""
from node_list import ListNode
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Base case. Empty, return
        if not head:
            return

        # Find mid pointer, then split for l1, l2 (contains mid)
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        return head

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3)
    n4 = ListNode(4); n5 = ListNode(5); n6 = ListNode(6); n7 = ListNode(7)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5; n5.next = n6; n6.next = n7

    print("Original Linked List:")
    n1.print_list(n1)

    curr = Solution().reorderList(head = n1)
    print("\nReordered Linked List:")
    curr.print_list(curr)

