"""
https://leetcode.com/problems/distinct-subsequences
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if (i, j) in memo:
                return memo.get((i, j))
            
            # if t end is reached first, count
            if j == len(t):
                return 1

            # if s end is reached first, do not count
            if i == len(s):
                return 0            

            # equal, explore paths
            if s[i] == t[j]:
                
                a = dfs(i + 1, j) # move only i to capture all possibilities
                b = dfs(i + 1, j + 1) # move both
                memo[(i, j)] = a + b
                return a + b
            
            # not equal, just move i
            else:
                return dfs(i + 1, j) # move only i to capture all possibilities
        
        memo = {}
        return dfs(0, 0)
            
            