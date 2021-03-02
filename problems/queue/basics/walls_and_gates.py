"""
https://leetcode.com/problems/walls-and-gates/
"""
from typing import List
from collections import deque
import math
class Solution:
    def wallsAndGates_CleanAttempt(self, rooms: List[List[int]]) -> None:
        # Run bfs starting from gates
        def bfs(i, j):

            queue = deque([(i, j, 0)])

            # Traverse in 4 directions for a matrix
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                curr = queue.pop()
                c_i = curr[0]
                c_j = curr[1]

                # Update distance + 1
                distance = curr[2] + 1

                for direction in directions:
                    i = c_i + direction[0]
                    j = c_j + direction[1]

                    # Constraint - out of bounds
                    if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]):
                        continue

                    # Constraint - at a gate or wall
                    if result[i][j] == 0 or result[i][j] == -1:
                        continue

                    # Constaint - if distance is greater than or equal to current result
                    if distance >= result[i][j]:
                        continue

                    # Update result with shortest distance if distance is less than current result
                    result[i][j] = distance

                    queue.append((i, j, distance))

            return

        result = rooms

        # Run BFS starting only from gates. That way you can populate shortest path to every room.
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(i, j)

        print(result)

























    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Determine shortest path from gate at every index.

        Do not return anything, modify rooms in-place instead.
        """
        def bfs(i, j):
            # Queue will consist of INDICES. Not element values.
            queue = deque()
            queue.append([i, j])

            # Indices movement for neighbors: Down, Up, Right, Left
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

                    # Constraints: (1) Out of bounds, (2) Value == 0 or Visited or current value <= prev value
                    if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] <= rooms[c_i][c_j] + 1:
                        continue

                    # Process element (current element should have +1 from previous element)
                    rooms[i][j] = rooms[c_i][c_j] + 1

                    # Add neighbor to queue
                    queue.append([i, j])

        gate_value = 0

        # Start at the gates. You'll calculate the distance at every open index (math.inf).
        # Queue will consist of INDICES. Not element values.
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == gate_value:
                    bfs(i, j)

        print(rooms)

if __name__ == '__main__':
    rooms = [[math.inf, -1, 0, math.inf],      # [3,-1,0,1]
             [math.inf, math.inf, math.inf, -1],      # [2,2,1,-1]
             [math.inf, -1, math.inf, -1],      # [1,-1,2,-1]
             [0, -1, math.inf, math.inf]]      # [0,-1,3,4]

    Solution().wallsAndGates_CleanAttempt(rooms)
