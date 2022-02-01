"""
https://quastor.org/cracking-the-coding-interview/linked-lists/return-kth-to-last

You are given a linked list as input. The linked list may or may not have a cycle. Write a function that returns the node at the beginning of the cycle (if it exists) or None.

Input - 1 -> 2 -> 3 -> 4 -> 2 (same 2 as earlier)
Output - 2
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head):
        """
        Two Pointer - fast, slow

        1->5->2->3->5->2 (same as old)
                 s
                 f

        1->5->2->3->5->7->2 (same as old)
                    s
                    f
        """
        slow = fast = head
        while slow:
            if not fast:
                return
            if not fast.next:
                return        
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
if __name__ == '__main__':

    d = ListNode(5)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(5, b)
    head = ListNode(1, a)
    d.next = b

    print(Solution().detectCycle(head))
