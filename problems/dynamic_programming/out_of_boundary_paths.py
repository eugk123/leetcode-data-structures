"""
https://leetcode.com/problems/out-of-boundary-paths/
"""
class Solution:
    """
    Top-down Memo Count Unique Paths
    
    4 paths: left, right, up, down

    return conditions
    1) moves < maxMoves, out of boundaries, -> return 1 (count)
    3) moves == maxMoves, out of boundaries, -> return 1 (count)
    3) moves == maxMoves, within boundaries, -> return 0 (don't count)

    memo contains i, j, and moves
    Time and Space O(n*m*M) where n #rows, m #cols, M #moves
    """
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def dfs(i, j, moves):
            # return 0/1
            if (i, j, moves) in memo:
                return memo.get((i, j, moves))
            
            # hit out of bounds, valid path
            if i < 0 or j < 0 or i == m or j == n:
                return 1
                
            # valid path, we reached n moves and hit out of bounds            
            if moves == maxMove:
                if i < 0 or j < 0 or i == m or j == n:
                    return 1
                else:
                    return 0
                
            # try unique paths            
            a = dfs(i + 1, j, moves + 1)
            b = dfs(i - 1, j, moves + 1)
            c = dfs(i, j + 1, moves + 1)
            d = dfs(i, j - 1, moves + 1)
            
            memo[(i, j, moves)] = a+b+c+d
            # sum up all paths
            return a+b+c+d
        
        memo = {}
        
        return dfs(startRow, startColumn, 0) % (10**9 + 7)