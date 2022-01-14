"""
https://quastor.org/cracking-the-coding-interview/linked-lists/return-kth-to-last

You're given a Linked List. Write a function to find the Kth to last node in that Linked List.

Input - 1 -> 2 -> 3 -> 4 -> 5 -> None, k = 2
Output - 4
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def returnKthFromLast(self, head, k):
        """
        Two Pointer k distance apart

        k = 5
        1->5->2->3->5->3->4->x
        c              n
           c              n
              c              n   Stop here as n is set to null
        {1,5,2,3,4}
        """
        curr = head
        nxt = curr
        # With k, place the pointer k spaces next. This will also tell you if the size of list is greater than k
        i = 0
        while i < k:
            nxt = nxt.next
            i += 1

            # Return none if k exceeds length of list
            if not nxt:
                return None

        # Traverse curr until next pointer goes null, this will be your result
        while nxt:
            nxt = nxt.next
            curr = curr.next

        return curr.val



if __name__ == '__main__':

    f = ListNode(4)
    e = ListNode(3, f)
    d = ListNode(5, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(5, b)
    head = ListNode(1, a)

    k = 5
    print("k = {}, less than length, resulting in: {}".format(k, Solution().returnKthFromLast(head, k)))
    k = 8
    print("k = {}, greater than length, resulting in: {}".format(k, Solution().returnKthFromLast(head, k)))