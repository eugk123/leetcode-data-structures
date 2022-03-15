"""
https://leetcode.com/problems/minimum-path-sum/
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo.get((i, j))

            # went out of bounds
            if i == len(grid) or j == len(grid[0]):
                return math.inf

            # we reached the end
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            
            # explore all paths
            right = grid[i][j] + dfs(i + 1, j)
            down = grid[i][j] + dfs(i, j + 1)
            
            memo[(i, j)] = min(right, down)
            return min(right, down)
        
        memo = {}
        return dfs(0, 0)