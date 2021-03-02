"""
https://leetcode.com/problems/flood-fill
"""
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        def dfs(i, j):
            # Constraint: Out of bounds
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return

            # Constraints: visited or not existing color
            if image[i][j] == new_color or image[i][j] != existing_color:
                return

            # Process
            image[i][j] = new_color

            # Traverse 4-directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Remember, you are only modifying existing colors which is based on your starting point
        existing_color = image[sr][sc]

        # Starting location (sr, sc). Flood from one location and that's it.
        dfs(sr, sc)

        return image