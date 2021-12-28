"""
https://leetcode.com/problems/shortest-bridge
"""
from typing import List
from collections import deque
class Solution:
    """
    DFS & BFS

    https://leetcode.com/problems/shortest-bridge/discuss/189321/Java-DFS-find-the-island-greater-BFS-expand-the-island
    """
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]):
                return

            if A[i][j] == 0 or A[i][j] == -1:
                return

            A[i][j] = -1
            queue.append((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

            return

        queue = deque([])

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs(i, j)
                    # print(A)
                    break
            # Element mutated to -1 and we need to break out of loop entirely.
            if A[i][j] == -1:
                break

        steps = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for direction in directions:
                    # Update indices
                    i = x + direction[0]
                    j = y + direction[1]

                    # If out of bounds, skip
                    if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]):
                        continue

                    # If visited, skip
                    if A[i][j] == -1:
                        continue

                    # Attempt to find shortest path
                    if A[i][j] == 1:
                        return steps

                    # Set to visited. We do this to prevent from visiting again.
                    A[i][j] = -1

                    # Traverse neighbors
                    queue.append((i, j))

            steps += 1