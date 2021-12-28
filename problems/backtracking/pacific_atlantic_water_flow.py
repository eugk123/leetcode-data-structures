"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
from typing import List
import math
class Solution:
    """
    https://www.youtube.com/watch?v=vSz5sT5LeQQ

    The approach is to flood from both oceans. The condition is to have the prev value <= current value.

    Simply take two different sets. Perform DFS from each side to populate both sets. Take the intersection of both sets.
    
    Time Complexity: O(mn)
    since we keep a visited set for each ocean, we only visit a cell if it is not visited before.
    For each ocean, the worst case is mn thus totally O(mn)

    Space Complexity: O(mn)
    For each DFS we need O(h) space used by the system stack, where h is the maximum depth of the recursion.
    In the worst case, O(h) = O(m*n) such that the grid map is filled with lands where DFS goes by M×N deep.
    Each visited set can have at maximum all cells from the matrix so O(mn). Two ocean means O(2mn).
    """
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not matrix:
            return []

        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])

        def traverse(i, j, prev, visited):
            # Conditions
            # If out of bounds, return
            if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
                return

            # Flood inwards from low to high, so if next number is less than previous, return
            if matrix[i][j] < prev:
                return

            # If visited, return
            if (i, j) in visited:
                return

            # Mark and update previous
            prev = matrix[i][j]
            visited.add((i, j))

            # Traverse
            traverse(i + 1, j, prev, visited)
            traverse(i - 1, j, prev, visited)
            traverse(i, j + 1, prev, visited)
            traverse(i, j - 1, prev, visited)

        for row in range(rows):
            traverse(row, 0, -math.inf, p_visited)
            traverse(row, cols - 1, -math.inf, a_visited)

        for col in range(cols):
            traverse(0, col, -math.inf, p_visited)
            traverse(rows - 1, col, -math.inf, a_visited)

        return list(p_visited & a_visited)

if __name__ == '__main__':
    print(Solution().pacificAtlantic(matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))