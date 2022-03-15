"""
https://leetcode.com/problems/path-sum-iii
"""
from node.node_tree import TreeNode
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
        https://www.youtube.com/watch?v=uZzvivFkgtM view approach 2
        
        Memorization of path sum

        Use a hashmap to store previous paths. We cannot use a set, because there could be node.val == 0, which allows for multiple paths to return the same value.

        if currentSum - targetSum in previousPathsMap:
            self.result += previousPathsMap[currentSum - targetSum]
        
        ex: 10 - 5 - 3 - 0
        ------        
        sum     prev_paths
        10      {}
        15      {10:1}
        18      {10:1, 15:1}
        18      {10:1, 15:2}

        Time and Space O(N)
        """
        def addPreviousPath(current_sum, previous_paths):
            if current_sum in previous_paths:
                previous_paths[current_sum] += 1
            else:
                previous_paths[current_sum] = 1
            return previous_paths
        
        def removePreviousPath(current_sum, previous_paths):
            if current_sum in previous_paths:
                previous_paths[current_sum] -= 1
            else:
                previous_paths[current_sum] = 0
            return previous_paths
                
        def dfs(root, current_sum, previous_paths):
            
            if current_sum == targetSum:
                self.result += 1
            if current_sum - targetSum in previous_paths:
                self.result += previous_paths[current_sum - targetSum]
            
            if root.left:
                previous_paths = addPreviousPath(current_sum, previous_paths)
                dfs(root.left, current_sum + root.left.val, previous_paths)
                previous_paths = removePreviousPath(current_sum, previous_paths)

            if root.right:
                previous_paths = addPreviousPath(current_sum, previous_paths)
                dfs(root.right, current_sum + root.right.val, previous_paths)
                previous_paths = removePreviousPath(current_sum, previous_paths)

            return
        
        self.result = 0
        
        if not root:
            return 0
        
        dfs(root, root.val, {}) # find all possible paths

        return self.result    
    
    def pathSumBruteForce(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Brute Force
        BFS & DFS double traversal

        Time O(N^2)
        Space O(N) - height of recursion stack N and size of queue N
        """
        def dfs(root, current_sum, current_path):
            
            
            if current_sum == targetSum:
                self.result += 1
            
            if root.left:
                dfs(root.left, current_sum + root.left.val, current_path + [root.left.val])
            if root.right:
                dfs(root.right, current_sum + root.right.val, current_path + [root.right.val])
            
            return
        
        self.result = 0
        
        if not root:
            return 0
        
        queue = deque([root])
        while queue:
            curr = queue.pop()
            dfs(curr, curr.val, [curr.val]) # find all possible paths
            
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
            
        return self.result