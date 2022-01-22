"""
https://leetcode.com/problems/add-two-numbers-ii/
"""
from node_list import ListNode
class Solution:
    """
    https://www.youtube.com/watch?v=71NkQBIHxg8
    Combination of Add Two Numbers and Reverse Linked List
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        carry = 0
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        while l1 or l2:
            # Get current values
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            # current sum with carry (1/0)
            sum = l1_val + l2_val + carry

            # appending listnode to the front (draw it out on the board!)
            if sum > 9:
                carry = 1
                remainder = sum - 10
                curr = ListNode(remainder)
            else:
                carry = 0
                curr = ListNode(sum)
            curr.next = head
            head = curr

            # Edge case. 1+9 = [1,0]
            if carry == 1 and sum > 9 and not l1 and not l2:
                curr = ListNode(1)
                curr.next = head
                head = curr
        return head

    def reverse(self, node: ListNode) -> ListNode:
        curr = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

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