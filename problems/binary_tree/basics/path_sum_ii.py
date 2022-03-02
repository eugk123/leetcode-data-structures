"""
https://leetcode.com/problems/path-sum-ii/
"""
from node.node_tree import TreeNode
class Solution:
    """
    Time and Space O(N)
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, current, path):
            # Check if path-to-leaf sum equals targetSum
            if not root.left and not root.right:
                if current == targetSum:
                    result.append(path)
                return
            
            if root.left:
                dfs(root.left, current + root.left.val, path + [root.left.val])
            
            if root.right:
                dfs(root.right, current + root.right.val, path + [root.right.val])
                
            return
        
        if not root:
            return []
        
        result = []
        dfs(root, root.val, [root.val])
        return result