"""
https://leetcode.com/problems/path-sum
"""
from node.node_tree import TreeNode
class Solution:
    """
    Time and Space O(N)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, current):
            # Check if path-to-leaf sum equals targetSum
            if not root.left and not root.right:
                if current == targetSum:
                    self.result = True
                return
            
            if root.left:
                dfs(root.left, current + root.left.val)
            
            if root.right:
                dfs(root.right, current + root.right.val)
                
            return
        
        if not root:
            return False
        
        self.result = False
        dfs(root, root.val)
        return self.result

    def hasPathSumOld(self, root: TreeNode, targetSum: int) -> bool:
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


        