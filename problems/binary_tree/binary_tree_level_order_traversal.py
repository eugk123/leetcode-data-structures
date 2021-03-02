"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from node_tree import TreeNode
from collections import deque
from typing import List
class Solution:
    """
    BFS is level order traversal.

    Return the level order list of list. So for each level, we can append the current level.
    Use deque for FIFO queues - popleft() is O(1) time vs list.pop(0) is O(n) time.
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        queue = deque([root])
        result = []
        while queue:
            level = []
            result.append(level)

            # We are setting this for loop for current elements in queue which should contain nodes
            # for current level.
            for _ in range(len(queue)):
                # Pop and add to current val to level array
                curr = queue.popleft()
                level.append(curr.val)

                # Traverse children for current level and add them to queue.
                # Range will not update. So we can keep appending to queue!
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(4)
    print(Solution().levelOrder(root))
