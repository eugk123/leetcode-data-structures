"""
https://leetcode.com/problems/minimum-height-trees/

This problem is very difficult to illustrate in text. Please refer to the link above.

Note that the solution returns a List because there can be 2 root node.
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=a4hXpeHZ_-c&t=1247s
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = dict()

        for i in range(n):
            adj[i] = []

        for edge in edges:
            adj.get(edge[0]).append(edge[1])
            adj.get(edge[1]).append(edge[0])

        # Initialize leaves array.
        leaves = []

        # Find all the leaves by searching through entire graph
        for i in range(n):
            if len(adj.get(i)) == 1:  # If node only has 1 neighbor, it's a leaf
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = adj[leaf].pop()
                # remove the only edge left
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves

if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n=6, edges=[[0,1],[1,2],[1,3],[1,4],[4,5]]))