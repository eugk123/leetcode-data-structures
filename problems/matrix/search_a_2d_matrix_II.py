"""
https://leetcode.com/problems/search-a-2d-matrix-ii
"""
from typing import List
class Solution:
    """
    Do not use DFS. This will traverse through the entire matrix O(m*n) time.

    Do not use binary search. This will require performing it at every row or column
    resulting in O(n log m) time

    Use process of elimination. Simply work from top right corner.
    When m[i][j] < target, move left
    When m[i][j] > target, move down.
    When target is found, return True
    When out of bounds return False
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1

        while i <= len(matrix) - 1 and j >= 0:
            # When m[i][j] > target, move down.
            if matrix[i][j] > target:
                j -= 1

            # When m[i][j] < target, move left
            elif matrix[i][j] < target:
                i += 1

            # When target is found, return True
            else:
                return True

        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[2,5],
                                          [2,8],
                                          [7,9],
                                          [7,11],
                                          [9,11]], target=7))