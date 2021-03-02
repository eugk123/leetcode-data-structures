"""
https://leetcode.com/problems/01-matrix/
"""
from typing import List
import collections
import math
import time
class Solution:
    """
    Use BFS w/ queue
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(queue):
            while queue:
                curr, distance = queue.popleft()
                curr_i = curr[0]
                curr_j = curr[1]

                distance = distance + 1

                # Traverse neighbors
                for direction in directions:
                    i = curr_i + direction[0]
                    j = curr_j + direction[1]

                    # Constraint - Out of bounds
                    if i < 0 or j < 0 or i >= rows or j >= cols:
                        continue

                        # Constraints - If visited or at another starting point (0) or distance is equal/greater, then skip
                    if (i, j) in visited or matrix[i][j] == 0 or distance >= result[i][j]:
                        continue

                    # Process - Make sure you can't visit this node again.
                    visited.add((i, j))

                    # And update result with new distance
                    result[i][j] = distance

                    # Add back into queue
                    queue.append(((i, j), distance))

        # Directions used for neighbors
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Keep track of visited nodes
        visited = set()

        # Queue contains indices and distance
        # Distance will start at 1.
        # (indices, distance) = ((0, 0), 1)
        queue = collections.deque()

        # Initialize results. Collect shortest paths here.
        rows, cols = len(matrix), len(matrix[0])
        result = [[math.inf] * cols for i in range(rows)]

        # Iterate through entire matrix, start only at 0, because you're calculating shortest path on all the other elements from each 0 and updating only when number is smaller than previous.
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    queue.append(((i, j), 0))

        # Start BFS.
        bfs(queue)

        return result

    def updateMatrix_TLE(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        This is a working solution, except it exceeds time limit in LeetCode. Why?

        Notice that I'm resetting the visiting set. This effectively forces the BFS to traverse all nodes over and over
        again... So to fix this, simply visit only once by adding all starting points from the get go.
        """
        def bfs(i, j):
            # Queue contains indices and distance
            # Distance will start at 1.
            # (indices, distance) = ((0, 0), 1)
            queue = collections.deque([((i, j), 0)])

            while queue:
                curr, distance = queue.popleft()
                curr_i = curr[0]
                curr_j = curr[1]

                distance = distance + 1

                # Traverse neighbors
                for direction in directions:
                    i = curr_i + direction[0]
                    j = curr_j + direction[1]

                    # Constraint - Out of bounds
                    if i < 0 or j < 0 or i >= rows or j >= cols:
                        continue

                        # Constraints - If visited or at another starting point (0) or distance is equal/greater, then skip
                    if (i, j) in visited or matrix[i][j] == 0 or distance >= result[i][j]:
                        continue

                    # Process - Make sure you can't visit this node again.
                    visited.add((i, j))

                    # And update result with new distance
                    result[i][j] = distance

                    # Add back into queue
                    queue.append(((i, j), distance))

        # Directions used for neighbors
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize results. Collect shortest paths here.
        rows, cols = len(matrix), len(matrix[0])
        result = [[math.inf] * cols for i in range(rows)]

        # Iterate through entire matrix, start only at 0, because you're calculating shortest path on all the other elements from each 0 and updating only when number is smaller than previous.
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    visited = set()  # Keep track of visited nodes.
                    bfs(i, j)

        return result


if __name__ == '__main__':
    matrix = [[0, 0, 1],
              [1, 1, 1],
              [1, 1, 1]]

    print(Solution().updateMatrix(matrix))
    print("\n")

    # Build a fat matrix for time complexity testing:
    matrix = [[1]*60 for i in range(100)]
    for i in range(100):
        matrix[i][0] = 0

    t = time.process_time()
    Solution().updateMatrix_TLE(matrix)
    elapsed_time = time.process_time() - t

    t_prime = time.process_time()
    Solution().updateMatrix(matrix)
    elapsed_time_prime = time.process_time() - t_prime

    # When comparing string concatenation vs using a list, the time seems the same.
    print("BFS slow:", elapsed_time)
    print("BFS optimized:", elapsed_time_prime)