"""
https://quastor.org/cracking-the-coding-interview/linked-lists/remove-duplicates

You're given an unsorted linked list as input. Write a function that removes duplicate items.

Input - 1 -> 2 -> 1 -> 5 -> 2 -> None
Output - 1 -> 2 -> 5 -> None
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeDuplicates(self, head):
        """
        Hashset + curr, prev pointers
        
        1->5->2->3->5->3->4->x
              p  c
                 p  c->c->c     Notice duplicates are found, so only current is traversing
                 3------->4     Prev points to the next
                          p  c
        {1,5,2,3,4}
        """
        # Edge case, just size one
        if not head.next:
            return head
        
        # Set to track duplicate letters
        duplicates = set()

        # Initailize pointers and prev letter into set
        prev = head
        curr = prev.next
        duplicates.add(prev.val)

        # Traverse until curr reaches end
        while curr:
            # Traverse only curr if duplicate found, also set prev to skip to the next (curr.next)
            if curr.val in duplicates:
                curr = curr.next
                prev.next = curr
            # Traverse both if not duplicate
            else:
                duplicates.add(curr.val)
                prev = prev.next
                curr = curr.next


if __name__ == '__main__':
    f = ListNode(4)
    e = ListNode(3, f)
    d = ListNode(5, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(5, b)
    head = ListNode(1, a)

    Solution().removeDuplicates(head)

    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
