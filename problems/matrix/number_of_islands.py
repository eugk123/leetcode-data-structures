"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
import collections
from typing import List


class Solution:
    """
    https://www.youtube.com/watch?v=nNGSZdx6F3M&list=PLujIAthk_iiO7r03Rl4pUnjFpdHjdjDwy&t=485s
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # Solution counter initialized.
        num_islands = 0

        # Go through the entire matrix and DFS when we see a '1'
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.sink_dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def sink_dfs(self, grid, i, j):
        # If we're out of bounds or on a '0', no need to DFS down this path anymore
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # Make sure we don't check this spot again. Sink it the island!
        grid[i][j] = '0'

        # All the possible paths we can DFS to from here:
        self.sink_dfs(grid, i + 1, j)
        self.sink_dfs(grid, i - 1, j)
        self.sink_dfs(grid, i, j + 1)
        self.sink_dfs(grid, i, j - 1)

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1"]
    ]
    print(Solution().numIslands(grid))
