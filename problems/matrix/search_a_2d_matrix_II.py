"""
https://leetcode.com/problems/search-a-2d-matrix-ii
"""
from typing import List
class Solution:
    """
    Use DFS - make sure to use visited matrix
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        seen = dict()

        def dfs(seen, i, j):
            # End when out of bounds
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return

            # End if seen. Need to use this tuple arrangement because we can have duplicate nubmers in matrix
            if seen.get((i, j)) == 1:
                return

            # End target is reached
            if matrix[i][j] == target:
                return True

            seen[(i, j)] = 1

            # Traverse right and down throughout the matrix
            return dfs(seen, i + 1, j) or dfs(seen, i, j + 1)

        if dfs(seen, 0, 0) is True:
            return True
        return False




if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[2,5],
                                          [2,8],
                                          [7,9],
                                          [7,11],
                                          [9,11]], target=7))