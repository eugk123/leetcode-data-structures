"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from node_tree import TreeNode
from typing import List
class Solution:
    """
    BFS is level order traversal. Therefore, we can simply add 1 to depth every time the level queue is updated.
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(root):
            if root is None:
                return 0
            queue = [root]
            level_list = []
            current_level_list = [root.val]
            while queue:
                level_list.append(current_level_list)
                current_level_list = []
                for _ in range(len(queue)):
                    curr = queue.pop(0)
                    if curr.left:
                        queue.append(curr.left)
                        current_level_list.append(curr.left.val)
                    if curr.right:
                        queue.append(curr.right)
                        current_level_list.append(curr.right.val)
            return level_list
        return bfs(root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(4)
    print(Solution().levelOrder(root))
