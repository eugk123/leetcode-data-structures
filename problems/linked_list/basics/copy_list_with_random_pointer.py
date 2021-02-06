"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def getCopy(node):
            # If node does not exist, return None
            if not node:
                return None

            else:
                # If node has not been visited/copied yet, add to map.
                if not visited.get(node):
                    visited[node] = Node(node.val, None, None)

                # If node exist, return deep copy
                return visited.get(node)

        if not head:
            return None

        curr = head

        # You need a map that stores curr and deep copies of curr to track if visited.
        # Don't bother with the indices. That serves no purpose in this problem.
        visited = dict()

        # Set previous pointer
        prev = curr

        # Deep copy first index and set to new_head and new_prev
        new_head = new_prev = getCopy(prev)

        # update deep copy random pointer.
        if prev.random:
            new_prev.random = getCopy(prev.random)

        # set curr one step ahead of prev
        curr = curr.next
        while curr:
            # Create deep copy of current node
            new_curr = getCopy(curr)

            # Set random pointer for deep copy
            # update deep copy random pointer.
            if curr.random:
                new_curr.random = getCopy(curr.random)

            # Set next pointer for deep copy
            new_prev.next = new_curr

            # Traverse (copied) prev node and current node
            new_prev = new_curr
            curr = curr.next

        return new_head