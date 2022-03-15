"""
https://leetcode.com/problems/longest-common-subsequence/submissions/
"""
class Solution:
    """
    
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i, j):
            # MEMO Get
            if (i, j) in memo:
                return memo.get((i, j))
            
            # When the end of text1 or text2 is reached, return 0
            if i == len(text1) or j == len(text2):
                return 0
            
            # Same letter, we have a common subsequence, count 1, and traverse both i and j
            if text1[i] == text2[j]:    
                return 1 + dfs(i + 1, j + 1)
            
            # Try all possible paths, don't count, and move either i or j
            else:
                a = dfs(i + 1, j)
                b = dfs(i, j + 1)
                
                # MEMO Add
                memo[(i, j)] = max(a, b)
                return max(a, b)
            
        # MEMO Init
        memo = {}
        return dfs(0, 0)