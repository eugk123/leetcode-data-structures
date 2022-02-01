"""
https://quastor.org/cracking-the-coding-interview/linked-lists/return-kth-to-last

You are given two singly linked lists. Write a function to determine if the two lists intersect. If they do intersect, return the node at which the two lists intersect. Otherwise, return None.

Input -
1 -> 2 -> 3 ->
               4 -> 5 -> 6
          2 ->

Output - 4 -> 5 -> 6
(the output is the node with the value 4)
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def findIntersectedNodes(self, h1, h2):
        """
        Constraints to think about. 
        Not all values in list are unique. You literally could have an input like this 1->1->1->1, 1->1->1 that intersects at final node.
        This means that we need to check if the objects are equal to confirm they are intersection NOT the value of the nodes.

        Two Pass - count length, the difference in length is where you will position the pointer on the longer list, then iterate till listnodes match
                 h2->2->
                        5->3->4->x
        h1->1->5->2->3->

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l1 = l2 = 0  # length
        c1, c2 = h1, h2
        
        # First pass, get total length, and set longer and shorter lists
        while c1 or c2:
            if c1:
                c1 = c1.next
                l1 += 1
            if c2:
                c2 = c2.next
                l2 += 1

        # Set the long and short pointers
        if l1 > l2:
            long, short = h1, h2
            diff_length = l1 - l2
        else:
            long, short = h2, h1
            diff_length = l2 - l1

        # Traverse long using the total difference in length
        for i in range(diff_length):
            long = long.next

        # Now that we are at equal lengths from tail, we check until list nodes match
        while long:
            if long == short:
                return long
            long = long.next
            short = short.next


if __name__ == '__main__':

    f = ListNode(4)
    e = ListNode(3, f)
    d = ListNode(5, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(5, b)
    h1 = ListNode(1, a)
    h2 = ListNode(2, d)

    curr = Solution().findIntersectedNodes(h1, h2)

    while curr:
        print("{}".format(curr.val, end = " "))
        curr = curr.next
