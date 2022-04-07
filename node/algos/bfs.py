"""
There is only iterative implementation of BFS.
Use for calculating shortest path.
"""
from collections import deque
from node.node_tree import TreeNode
def bfs_tree(root: TreeNode):
    queue = deque([root])  # Initialize deque with root

    while queue:
        for _ in range(len(queue)):
            # Pop first index (FIRST OUT)
            curr = queue.popleft()

            # Do something - Remove print statement
            print(curr.val, end=" ")

            # Append children to queue (FIRST IN - left, then right)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

from node_graph import Node
def bfs_graph(root: Node):
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            # Do something - Remove print statement
            print(curr.val, end=" ")

            # Append neighbors to queue (instead of children in a binary_tree)
            for nei in curr.neighbors:
                queue.append(nei)

def bfs_graph_w_visited(root: Node):
    queue = deque([root])
    visited = set(root)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            # Do something - Remove print statement
            print(curr.val, end=" ")

            # Append neighbors to queue (instead of children in a binary_tree)
            for nei in curr.neighbors:

                # Constraint - Visited, skip
                if nei in visited:
                    continue

                # Process - Add neighbor to visited
                visited.add(nei)

                queue.append(nei)

from typing import List
def bfs_matrix(visited, matrix: List[List[int]], i, j):
    # Queue will consist of INDICES. Not element values.
    queue = deque()
    queue.append([i, j])

    # Process - add to visited
    visited.add((i, j))

    # Indice movement for neighbors: Down, Up, Right, Left
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

            # Constraints: (1) Out of bounds, (2) Value == 0 or Visited
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == "0" or (i, j) in visited:
                continue

            # Process - add to visited
            visited.add((i, j))

            # Add neighbor to queue
            queue.append([i, j])

if __name__ == '__main__':
    # Tree
    print("BFS Iterative Tree")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    bfs_tree(root)


    # Graph
    print("\nBFS Iterative Graph")
    root = n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n4, n5]

    bfs_graph(root)

    # Matrix
    print("\nBFS Iterative Matrix")
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    bfs_matrix(matrix)
