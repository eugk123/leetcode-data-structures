"""
https://leetcode.com/problems/add-two-numbers-ii/
"""
from node_list import ListNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Summation of two lists are done with it's ends aligned. So work from the end and add.
        head = ListNode(0)  # Create dummy head pointer
        curr = head  # Set this to prev. You need prev to allow creation of resultant list
        carry = 0
        while l1 or l2:
            # Get sum.
            if l1 and l2:
                value = l1.val + l2.val
            elif l1 and not l2:
                value = l1.val
            else:
                value = l2.val

            # Set next pointer to new node (make sure it's of modulus 10 in case greater than 10)
            curr.next = ListNode((value + carry) % 10)

            # Determine if there is a carryover of 1 (happens if remainder of modulus 10 is present from previous value).
            if value + carry >= 10:
                carry = 1
            else:
                carry = 0

            # Traverse all pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        # We know if the total value is greater or equal than 10 at the end, we need to add another node of value 1.
        if value + carry >= 10:
            curr.next = ListNode(1)

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

