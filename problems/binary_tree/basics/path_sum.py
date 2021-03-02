"""
https://leetcode.com/problems/path-sum
"""
from node_tree import TreeNode
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(current_sum, root):
            # Update sum
            if root:
                current_sum = current_sum + root.val

            # If leaf node and sum equal to target sum, return True
            if not root.left and not root.right and current_sum == targetSum:
                return True

            if root.left and dfs(current_sum, root.left) is True:
                return True
            if root.right and dfs(current_sum, root.right) is True:
                return True

            return False

        if not root:
            return None
        return dfs(0, root)