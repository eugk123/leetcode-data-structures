"""
https://leetcode.com/problems/add-two-numbers-ii/
"""
from node.node_list import ListNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        carry = 0

        # Get sum and traverse through both l1 and l2
        while l1 or l2:  # while l1 or l2 is not empty

            # Get l1 and l2 values, then traverse. We set to 0 if curr = None.
            if l1:  # while l1 is not empty
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:  # while l2 is not empty
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            sum = l1_val + l2_val + carry
            if sum > 9:
                carry = 1
                remainder = sum - 10
                curr.next = ListNode(remainder)
            else:
                carry = 0
                curr.next = ListNode(sum)
            curr = curr.next

            # If we need to carry over to an extra index even when both lls are traversed to null, we need to add another element of value 1
            if carry == 1 and not l1 and not l2:
                curr.next = ListNode(1)
                break

        # Return head starting from 2nd index since 1st index is dummy node
        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(2)
    l2.next = ListNode(2)
    l2.next.next = ListNode(6)

    curr = Solution().addTwoNumbers(l1, l2)
    print("Printing Linked List:")
    while curr:
        print(curr.val)
        curr = curr.next

