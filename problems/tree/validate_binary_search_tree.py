"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
import math
from node_tree import TreeNode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs_in_order(root):
            if root == None:
                return
            if dfs_in_order(root.left) is False:
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            if dfs_in_order(root.right) is False:
                return False

        self.prev = -math.inf
        if dfs_in_order(root) is False:
            return False
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().isValidBST(root))