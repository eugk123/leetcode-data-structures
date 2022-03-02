"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
class Solution:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

              1
            /   \
         -2      2
        /   \
      4       3
      
    All leaf nodes return it's current value
    dfs(4) = 2, dfs(3) = 3, dfs(2) = 2
    
    All non-leaf nodes return the maxSum of the following:
    node.val or node.val + leftSum or node.val + rightSum
    dfs(-2) = max(-2, -2 + 4, -2 + 3) = 2
    
    It is also important to calculate the potential path of 4 -> -2 -> 3
    We take that path and compare with global max sum.
    currentSum = leftSum + node.val + rightSum = 4 + -2 + 3 = 5 
    self.maxSum = max(self.maxSum, currentSum) = 5
    
    Here is another non-leaf node working up
    dfs(1) = max(1, 1 + 2, 1 + 2) = 3
    currentSum = 2 + 1 + 2 = 5
    self.maxSum = 5
    
    If every number is negative, the maxSum is going to be the single node with the smallest negative number found at it's root at runtime
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Empty node returns 0
            if not node:
                return 0
            
            # Take maxSum of left and right side; these will recursively be returned upwards
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            
            # CS = node.val + LS + RS. This is not a returnable path. We check to see if this is the maxSum.
            current_sum = node.val + left_sum + right_sum            
            self.max_sum = max(self.max_sum, current_sum)
            
            # path up is going to be the max of one of the following:
            # max(node.val, node.val + LS, node.val + RS)
            return node.val + max(left_sum, right_sum)
        
        if not root:
            return 0
        
        self.max_sum = -math.inf        
        dfs(root)
        return self.max_sum