"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Your code should preferably run in O(n) time and use only O(1) memory.

        Return null if no intersection

        Use hash set. We can store pointers in this set. We can check if they share the same pointer
        with the set. Return the pointer if matched!
        """
        A = headA
        B = headB
        nodesSeen = set()

        while A:
            nodesSeen.add(A)
            A = A.next

        while B:
            if B in nodesSeen:
                return B
            B = B.next

        return None