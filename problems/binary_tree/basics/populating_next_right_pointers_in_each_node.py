"""
leetcode.com/problems/populating-next-right-pointers-in-each-node
"""
import collections
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    """
    Same problem as https://leetcode.com/problems/binary-tree-level-order-traversal/ but with just an additional
    work to point the new next pointer to the next node of the current level.
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = collections.deque([root])

        root.next = None  # Root node must point to null
        while queue:

            # On a per level basis, you're going to point each node to the right of the next node in the current queue.
            prev = None  # Need to assign a reference to prev pointer
            for _ in range(len(queue)):
                curr = queue.popleft()

                if prev:
                    prev.next = curr

                # Populate queue with children for next level traversal
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev = curr  # Update previous
            prev.next = None  # Final node of the previous level must point to null

        return root