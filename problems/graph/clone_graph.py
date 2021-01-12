"""
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
- For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
- Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
- The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

:param node:
:return:
"""
from node.node_graph import Node
class Solution:
    """
    https://www.youtube.com/watch?v=f2EfGComRKM&t

    Perform DFS using a visited hashmap {node -> copy}
    """
    def cloneGraph(self, node):
        def dfs(node):
            # Base case - if empty, return the node or None
            if not node:
                return node

            # If the node was already visited before
            # Return the clone from the visited dictionary.
            if node in visited:
                return visited[node]

            # Create copy and add to visited dict
            copy = Node(node.val)
            visited[node] = copy

            # Traverse through neighbors
            for nei in node.neighbors:
                # Create copy
                copy_nei = dfs(nei)

                # Append copied neighbor to current copied node
                if copy_nei:
                    copy.neighbors.append(copy_nei)
            return copy

        # Base case - empty
        visited = {}
        return dfs(node)

if __name__ == '__main__':
    node = n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2, n3]
    copy = Solution().cloneGraph(node)

    node.dfs_print()