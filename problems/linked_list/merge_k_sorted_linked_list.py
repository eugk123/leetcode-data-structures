"""
https://leetcode.com/problems/merge-k-sorted-lists
"""
from node.node_list import ListNode
from typing import List
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

        # List is null
        if lists is None or len(lists) == 0:
            return None

        # The solution is to merge two lists within the total number of lists.
        # So for example, 4 total lists -> 2 total lists -> 1 total list. Since we're cutting in half everytime,
        # this is O(logk) time complexity, where k is the total number of lists
        # Since the merge iterates through the entire list, that is O(N) time complexity where N is the total number of elements
        while len(lists) > 1:
            mergedList = []

            # Take every two adjacent lists using range function.
            for i in range(0, len(lists), 2):
                # For odd number of lists, the last iteration will not have a 2nd list. Need to check for that.
                # Having None is completely fine. The mergeTwoList will still work for empty lists.
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedList.append(mergeTwoLists(l1, l2))
            lists = mergedList
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
