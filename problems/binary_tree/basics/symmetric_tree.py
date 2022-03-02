"""
https://leetcode.com/problems/symmetric-tree/
"""
from node.node_tree import TreeNode
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            # If one side is empty and other is not, return False
            if not left and right:
                return False
            if left and not right:
                return False
            if not left and not right:
                return True

            # If values of left child is not equal to right child, then False
            if left.val != right.val:
                return False

            if dfs(left.left, right.right) is False:
                return False
            if dfs(left.right, right.left) is False:
                return False
            return True

        # If root is None, then symmetric
        if not root:
            return True

        left = root.left
        right = root.right

        return dfs(left, right)