"""
https://leetcode.com/problems/distinct-subsequences
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        We are looking for TOTAL UNIQUE PATHS. So we only COUNT at the boundary conditions!

        DO NOT COUNT IN THE DFS STATEMENT (ex: 1 + dfs(i + 1, j + 1))

        Time O(N*M) where n = len(s) and t = len(t)
        Space O(N*M)
        """
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
            a = 0
            if s[i] == t[j]:
                a = dfs(i + 1, j + 1) # move both
            
            # either equal or not equal, just move i; to capture all possibilities
            b = dfs(i + 1, j) 

            memo[(i, j)] = a + b
            return a + b
        
        memo = {}
        return dfs(0, 0)
            
            