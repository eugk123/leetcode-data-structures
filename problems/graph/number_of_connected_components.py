"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n node labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of node), write a function
to find the number of connected components in an undirected graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4
Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3
Output:  1

Note:
    You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as
    [1, 0] and thus will not appear together in edges.
"""
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=a4hXpeHZ_-c&t=267s
        """
        # Sets up the adjacency list populating with node' neighbors
        adj = dict()
        for i in range(n):  # Add node.val (key) with empty neighbors (val)
            adj[i] = []
        for i in range(len(edges)):  # Add edges into neighbors
            adj.get(edges[i][0]).append(edges[i][1])
            adj.get(edges[i][1]).append(edges[i][0])

        # Create a visited array, where 0 = unvisited and 1 = visited
        visited = [0] * n

        # Count is the number of connected components
        count = 0

        # Attempt to DFS from each node, so we find the different connected components
        for i in range(n):
            if visited[i] == 0:
                count += 1
                self.dfs(adj, i, visited)

        return count

    def dfs(self, adj, index, visited):
        # Constraint - Visited
        if visited[index] == 1:
            return

        # Mark the current node as visited
        visited[index] = 1

        # Get all the neighbors of this node
        for neighbor in adj.get(index):
            self.dfs(adj, neighbor, visited)

if __name__ == '__main__':
    print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))