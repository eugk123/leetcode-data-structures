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
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Use deque for FIFO queues - popleft() is O(1) time vs list.pop(0) is O(n) time.
        """
        if not root:
            return None
        queue = deque([root])
        level_list = []
        current_level_list = [root.val]
        while queue:
            level_list.append(current_level_list)
            current_level_list = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    current_level_list.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    current_level_list.append(curr.right.val)
        return level_list


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(4)
    print(Solution().levelOrder(root))
