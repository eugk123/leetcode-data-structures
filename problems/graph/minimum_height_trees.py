"""
https://leetcode.com/problems/minimum-height-trees/

This problem is very difficult to illustrate in text. Please refer to the link above.

Note that the solution returns a List because there can be 2 root node.
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=a4hXpeHZ_-c&t=1247s

    Implementation:
    Given the above algorithm, we could implement it via the Breadth First Search (BFS) strategy,
    to trim the leaf node layer by layer (i.e. level by level).
    - Initially, we would build a graph with the adjacency list from the input.
    - We then create a queue which would be used to hold the leaf node.
    - At the beginning, we put all the current leaf node into the queue.
    - We then run a loop until there is only two node left in the graph.
    - At each iteration, we remove the current leaf node from the queue. While removing the node,
      we also remove the edges that are linked to the node. As a consequence, some of the non-leaf node would become
      leaf node. And these are the node that would be trimmed out in the next iteration.
    - The iteration terminates when there are no more than two node left in the graph, which are the desired centroids node.
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

        # Keep removing leaves until there's at most 2 node left on the graph
        while n > 2:
            # Update total number of node in teh graph after we remove leaves
            n -= len(leaves)

            # Temporary array to hold new leaves
            new_leaves = []

            # Remove leaves from graph
            for i in leaves:
                print(adj)
                # Go to the leave's neighbors and remove entry from list
                leaf_index = adj.get(i)[0]
                adj.get(leaf_index).remove(i)

                # Remove leaf from graph key
                adj.pop(i)

                # If that neighbor only has one neighbor left, it's a leaf now.
                if len(adj.get(leaf_index)) == 1:
                    new_leaves.append(leaf_index)

            leaves = new_leaves
        return leaves


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n=6, edges=[[0,1],[1,2],[1,3],[1,4],[4,5]]))