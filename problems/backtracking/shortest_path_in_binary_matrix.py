"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
from typing import List
class Solution:
    """
    Shortest Path -> Simple BFS
    
    Time and Space O(n) where n is number of elements on grid
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # shortest path -> bfs
        # 8 ways to traverse
        directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        # result is min count
        result = math.inf
        
        # in queue, store (i,j,count). start at 0,0
        queue = deque([(0,0,1)])
        n = len(grid)
        
        if grid[0][0] == 1:
            return -1
        if grid[n-1][n-1] == 1:
            return -1
        if grid[0][0] == 0 and len(grid) == 1:
            return 1
        while queue:
            i, j, count = queue.popleft()
                
            for direction in directions:
                # update current i and j
                c_i = i + direction[0]
                c_j = j + direction[1]
                
                # end is reached, update count
                if c_i == n - 1 and c_j == n - 1:
                    result = min(result, count + 1)
                    
                # out of bounds constraint
                if c_i < 0 or c_i > n - 1 or c_j < 0 or c_j > n - 1:
                    continue
                
                # not valid path or visited constraint
                if grid[c_i][c_j] == 1:
                    continue
                
                # mark as visited, so can't go backwards
                grid[c_i][c_j] = 1

                # next level
                queue.append((c_i, c_j, count + 1))
        
        if result == math.inf:
            return -1
        return result