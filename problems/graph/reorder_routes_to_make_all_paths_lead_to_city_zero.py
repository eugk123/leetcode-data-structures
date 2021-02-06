"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""
from node_graph import Node
from typing import List
class Solution:
    """
    Directed Graph. Solve using DFS

    The trick here is to start from node 0 and work your way outwards. Count the number of times when edge is going
    the outward way.
    """
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(index):
            visited[index] = 1

            for neighbor, cost in adj.get(index):
                if visited[neighbor] == 0:
                    self.ans += cost
                    dfs(neighbor)

        self.ans = 0

        adj = dict()
        for i in range(n):
            adj[i] = []
        for edge in connections:
            adj[edge[0]].append((edge[1], 1))  # Out - add cost - to know this is the original directed graph
            adj[edge[1]].append((edge[0], 0))  # In - 0 cost - to know this is the opposite direction, but helps with traversal


        # Visited array
        visited = [0] * n

        # Perform DFS on only zero
        dfs(0)

        return self.ans

if __name__ == '__main__':
    print(Solution().minReorder(n=6, connections=[[0,1],[1,3],[2,3],[4,0],[4,5]]))
