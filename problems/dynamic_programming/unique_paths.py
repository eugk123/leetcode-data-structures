"""
https://leetcode.com/problems/unique-paths
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo.get((i, j))
            
            # Out of bounds, don't count
            if i == m or j == n:
                return 0
            
            # End is reached, count
            if i == m - 1 and j == n - 1:
                return 1
            
            # Try all paths.
            # Can only go two directions: right or down
            a = dfs(i + 1, j) # right
            b = dfs(i, j + 1) # down
            
            memo[(i, j)] = a + b
            return a + b
        
        memo = {}
        return dfs(0, 0)