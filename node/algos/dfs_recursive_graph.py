"""
This is the recursive implementation of DFS.
Use for finding combinations and exhausting all possibilities.
"""
from node_tree import TreeNode
def dfs_tree(node: TreeNode):
    # Constraint: Visited
    if node in visited:
        return

    # Do something - Add to visited
    visited.add(node)
    print(node.val, end=" ")

    # Traverse neighbors
    if node.left:
        dfs_tree(node.left)
    if node.right:
        dfs_tree(node.right)


from node_graph import Node
def dfs_graph(node):
    # Constraint: Visited
    if node in visited:
        return

    # Do something - Add to visited
    visited.add(node)
    print(node.val, end=" ")

    # Traverse neighbors
    for nei in node.neighbors:
        dfs_graph(nei)

def dfs_matrix(matrix, i, j):
    # Constraints: Out of bounds
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return

    # Constraint: Visited set
    if (i, j) in visited:
        return

    # Process: Add to Visited
    visited.add((i, j))

    # Traverse 4-ways
    dfs_matrix(matrix, i + 1, j)
    dfs_matrix(matrix, i - 1, j)
    dfs_matrix(matrix, i, j + 1)
    dfs_matrix(matrix, i, j - 1)

if __name__ == '__main__':
    print("\nDFS Recursive Tree")
    visited = set()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    dfs_tree(root)


    # Graph
    print("\nDFS Recursive Graph")
    visited = set()
    root = n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n4, n5]

    target = n5
    dfs_graph(root)

