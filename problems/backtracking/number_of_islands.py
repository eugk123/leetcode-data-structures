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
    
    Time Complexity: O(mn)
    Since we only visit a cell if it is not visited before, the worst case is mn thus totally O(mn).

    Space Complexity: O(mn)
    For each DFS we need O(h) space used by the system stack, where h is the maximum depth of the recursion.
    In the worst case, O(h) = O(m*n) such that the grid map is filled with lands where DFS goes by M×N deep.
    
    By marking visited positions, we only visit each position once with this algorithm. The resulting space is also the same size of the input m*n matrix.
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
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            # Sink current index
            grid[i][j] = '0'

            # Perform BFS. The trick is to use the directions (left, right, up, down) to iterate through the neighbors.
            # Figure out your constraints (out of bounds, gates, shortest path). Then process element
            while queue:
                ci, cj = queue.popleft()

                # Traverse neighboring elements
                for direction in directions:
                    # Update current indices with direction you are going
                    i = ci + direction[0]
                    j = cj + direction[1]

                    # Constraints: (1) Out of bounds
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                        continue

                    if grid[i][j] == '0':
                        continue
                    grid[i][j] = '0'

                    # Add neighbor to queue
                    queue.append([i, j])

        count = 0
        
        # Start only at land (val = 1). Since we're counting number of islands,
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count

    def numIslandsBfsVisited(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            # Queue will consist of INDICES. Not element values.
            queue = collections.deque()
            queue.append([i, j])

            # Indice movement for neighbors: Down, Up, Right, Left
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            # visit current index
            visited.add((i, j))


            # Perform BFS. The trick is to use the directions (left, right, up, down) to iterate through the neighbors.
            # Figure out your constraints (out of bounds, gates, shortest path). Then process element
            while queue:
                ci, cj = queue.popleft()

                # Traverse neighboring elements
                for direction in directions:
                    # Update current indices with direction you are going
                    i = ci + direction[0]
                    j = cj + direction[1]

                    # Constraints: (1) Out of bounds
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                        continue

                    # if not island, skip
                    if grid[i][j] == '0':
                        continue
                    
                    # if visited, skip
                    if (i, j) in visited:
                        continue
                    
                    # visit all islands
                    visited.add((i, j))

                    # Add neighbor to queue
                    queue.append([i, j])

        count = 0
        visited = set()
        
        # # Start only at land (val = 1). Since we're counting number of islands,
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
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
