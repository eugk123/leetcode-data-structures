"""
https://leetcode.com/problems/house-robber-iii
"""
class Solution:
    """
    https://www.youtube.com/watch?v=nHR8ytpzz7c
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if index in memo:
                return memo.get(self.index)
            
            if not root:
                return [0,0]                
            
            self.index += 1
            left = dfs(root.left)
            right = dfs(root.right)
            
            # to rob, add root.val
            rob = root.val + left[1] + right[1]

            # not to rob, do not add root, but take the maximum left and right
            not_rob = max(left) + max(right)
            
            memo[self.index] = [rob, not_rob]
            return [rob, not_rob]   # [with root, without root]
        
        self.index = 0
        memo = {}
        return max(dfs(root))