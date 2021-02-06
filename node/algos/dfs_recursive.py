"""
This is the recursive implementation of DFS.
Use for finding combinations and exhausting all possibilities.
"""
from node_tree import TreeNode
def dfs(root: TreeNode):
    return

from node_graph import Node
def dfs_graph_node(node):
    # Constraint: Visited
    if node in visited:
        return

    # Do something - Add to visited
    visited.add(node)
    print(node.val, end=" ")

    # Traverse neighbors
    for nei in node.neighbors:
        dfs_graph_node(nei)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    dfs(root)


    # Graph
    print("\nDFS Recursive Graph Node")
    visited = set()
    root = n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n4, n5]

    target = n5
    dfs_graph_node(root)

