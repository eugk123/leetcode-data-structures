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
        def sink_dfs(i, j):
            # If we're out of bounds or on a '0', no need to DFS down this path anymore
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return

            # Make sure we don't check this spot again. Sink it the island!
            grid[i][j] = '0'

            # All the possible paths we can DFS to from here:
            sink_dfs(i + 1, j)
            sink_dfs(i - 1, j)
            sink_dfs(i, j + 1)
            sink_dfs(i, j - 1)

        # Solution counter initialized.
        num_islands = 0

        # Go through the entire matrix and DFS when we see a '1'
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    sink_dfs(i, j)
                    num_islands += 1

        return num_islands


    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            # Queue will consist of INDICES. Not element values.
            queue = collections.deque()
            queue.append([i, j])

            # Indice movement for neighbors: Down, Up, Right, Left
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # Perform BFS. The trick is to use the directions (left, right, up, down) to iterate through the neighbors.
            # Figure out your constraints (out of bounds, gates, shortest path). Then process element
            while queue:
                curr = queue.popleft()

                # Grab current row and col indices
                c_i = curr[0]
                c_j = curr[1]

                # Traverse neighboring elements
                for direction in directions:
                    # Update current indices with direction you are going
                    i = c_i + direction[0]
                    j = c_j + direction[1]

                    # Constraints: (1) Out of bounds, (2) Value == 0 or Visited
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
                        continue

                    # Process - add to visited
                    visited.add((i, j))

                    # Add neighbor to queue
                    queue.append([i, j])

        visited = set()
        count = 0

        # Start only at land (val = 1). Since we're counting number of islands,
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    bfs(i, j)

        return count

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1"]
    ]
    print(Solution().numIslands(grid))

    grid = [
        ["1", "1", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "1", "0"]
    ]
    print(Solution().numIslandsBfs(grid))
