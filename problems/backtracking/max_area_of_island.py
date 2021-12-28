"""
https://leetcode.com/problems/max-area-of-island/
"""
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            # Constraint - out of bounds
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return

            # Constraint - sunk, return
            if grid[i][j] == 0:
                return

            # Process
            grid[i][j] = 0

            # Increase count and calculate max
            self.count += 1
            self.max_count = max(self.count, self.max_count)

            # Traverse
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return

        if not grid:
            return 0

        self.max_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Need to instantiate and reset count outside of the recursive stack.
                    # When doing dfs(i, j, count+1), this fails because you can't traverse back to grid[i][j]
                    # to reach other land once it's sunk.
                    self.count = 0
                    dfs(i, j)

        return self.max_count