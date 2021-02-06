"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    """
    https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/154908/Python-easy-solution-using-stack
    """
    def flattenDfsIterative(self, head: 'Node') -> 'Node':
        if not head:
            return None

        root = head
        stack = [root]

        # Initialize a prev pointer (set to None to retain same doubly linked list)
        prev = None
        while stack:
            curr = stack.pop()

            # link prev with current (conditional used to ignore prev=None)
            if prev:
                prev.next = curr
                curr.prev = prev
            prev = curr

            if curr.next:  # append opposite direction
                stack.append(curr.next)
            if curr.child:  # append first direction afterwards
                stack.append(curr.child)
                curr.child = None

        return head

    def flattenRecursive(self, head: 'Node') -> 'Node':
        """
        I wrote this solution. The trick is to iteratively write out the solution. Then find the recursive relationship.
        When building your recursive method, target finding the input variables and output.

        Time complexity is O(n) and space complexity is O(h) where h is the # of levels / depth of recursive calls.
        """

        curr = head

        def flattenLevel(curr):
            if head is None:
                return []

            # Traversing current level, when child is not none, store the current and next pointer.
            while curr:
                left = curr
                right = curr.next

                if curr.child:
                    # Initialize child left pointers
                    left_child = curr.child

                    # At left pointer index, Arrange connection between current and left pointer.
                    left.next = left_child
                    left_child.prev = left

                    # Traverse child level, when child is not none, store the current pointer which will satisfy the right child.
                    right_child = flattenLevel(curr.child)

                    # If right is none, then right_child points to None
                    # At right pointer index where inner.next is None, Arrange connection between next and right pointer.
                    if right:
                        right_child.next = right
                        right.prev = right_child
                    else:
                        right_child.next = None

                    # Set children child pointers to None
                    left.child = None

                curr = curr.next

            # left is essentially previous. You do not want to return curr because it is null at the end of the while loop.
            return left

        flattenLevel(curr)
        return head


if __name__ == '__main__':
    # 1 - 2 - 3 - NULL
    #     |
    #     4 - 5 - 6 - NULL
    # Desired Outcome: 1 - 4 - 5 - 6 - 2 - 3
    n1 = Node(val=1, prev=None, next=None, child=None)
    n2 = Node(val=2, prev=None, next=None, child=None)
    n3 = Node(val=3, prev=None, next=None, child=None)
    n4 = Node(val=4, prev=None, next=None, child=None)
    n5 = Node(val=5, prev=None, next=None, child=None)
    n6 = Node(val=6, prev=None, next=None, child=None)
    n1.next = n2; n2.prev = n1
    n2.next = n3; n3.prev = n2
    n3.next = n4; n4.prev = n3

    n2.child = n5;

    n5.next = n6; n6.prev = n5

    curr = Solution().flattenDfsIterative(head=n1)
    print("go forward:")
    while curr.next:
        print(curr.val)
        curr = curr.next

    print("go backwards:")
    while curr:
        print(curr.val)
        curr = curr.prev