"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
"""
from node_list import ListNode
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        # Traverse through both linked lists. Compare values.
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # At the end, there will be one list that has 1 node remaining.
        if l1 is not None:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = x1 = ListNode(1); x2 = ListNode(2); x3 = ListNode(3); x4 = ListNode(4)
    x1.next = x2; x2.next = x3; x3.next = x4

    y = y1 = ListNode(1); y2 = ListNode(3); y3 = ListNode(4)
    y1.next = y2; y2.next = y3

    print("List X:")
    x.print_list(x)

    print("\nList Y:")
    y.print_list(y)

    print("\nMerged List:")
    head = Solution().mergeTwoLists(x, y)
    head.print_list(head)


