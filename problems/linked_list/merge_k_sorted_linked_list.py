"""
https://leetcode.com/problems/merge-k-sorted-lists
"""
from node.node_list import ListNode
from typing import List
from math import ceil
class Solution:
    """
    Continuation of Merge Two Lists problem.

    The idea is for each iteration, combine every two adjacent lists for k sorted lists, until you have one final list.

    Return that final list, then done!
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(l1, l2):
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

        # Empty List
        if not lists:
            return None

        # Merge every two lists. Every iteration, you'll notice the length divides by two.
        # You do this until the length == 1.
        length = len(lists)
        while length != 1:

            # Notice this works perfectly for even cases.
            if length % 2 == 0:
                # Each merge divides the length by 2. If it's an odd length, it would be ceil(L/2)
                length = ceil(length / 2)

                # Iterate up to the zero-based halved length and merge every two lists.
                i = 0

                while i <= length - 1:  # 0, 1
                    lists[i] = mergeTwoLists(lists[2 * i], lists[2 * i + 1])
                    i += 1

            # Whenever we have odd number of lists, we need to perform one less iteration and add the final list
            # at the end because it has nothing to merge with
            else:
                # Each merge divides the length by 2. If it's an odd length, it would be ceil(L/2)
                length = ceil(length / 2)

                # Iterate up to the zero-based halved length and merge every two lists.
                i = 0

                while i <= length - 2:  # 0
                    lists[i] = mergeTwoLists(lists[2 * i], lists[2 * i + 1])
                    i += 1
                lists[i] = lists[2 * i]  # Add last list at the end.

        return lists[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = x1 = ListNode(1); x2 = ListNode(2); x3 = ListNode(3); x4 = ListNode(4)
    x1.next = x2; x2.next = x3; x3.next = x4

    y = y1 = ListNode(1); y2 = ListNode(3); y3 = ListNode(8)
    y1.next = y2; y2.next = y3

    z = z1 = ListNode(4); z2 = ListNode(5); z3 = ListNode(6)
    z1.next = z2; z2.next = z3

    print("List X:")
    x.print_list(x)

    print("\nList Y:")
    y.print_list(y)

    print("\nList z:")
    z.print_list(z)

    print("\nMerged K List:")
    head = Solution().mergeKLists(lists=[x, y, z])
    head.print_list(head)
