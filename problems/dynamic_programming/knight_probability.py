"""
https://leetcode.com/problems/knight-probability-in-chessboard/
"""
class Solution:
    """
    Recursion Relationship - 8 mov
    """
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        def dfs(i, j, moves):
            if (i, j, moves) in memo:
                return memo.get((i, j, moves))
            
            # if out of bounds, return 0
            if i < 0 or j < 0 or i >= n or j >= n:
                return float(0)
            
            if moves == k:
                return float(1)
            
            # for as long as moves < k, we traverse all 8 possible spots
            # continue to add total possible spots
            a = dfs(i + 1, j + 2, moves + 1)
            b = dfs(i + 1, j - 2, moves + 1)  
            c = dfs(i - 1, j + 2, moves + 1)
            d = dfs(i - 1, j - 2, moves + 1)
            e = dfs(i + 2, j - 1, moves + 1)
            f = dfs(i + 2, j + 1, moves + 1)
            g = dfs(i - 2, j - 1, moves + 1)
            h = dfs(i - 2, j + 1, moves + 1)
            
            memo[(i, j, moves)] = (a + b + c + d + e + f + g + h)/8
            return (a + b + c + d + e + f + g + h)/8
                
        memo = {}
        return dfs(row, column, 0)