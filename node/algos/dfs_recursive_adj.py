def traverse_edge_list(n, edges):
    """
    These type of problems will give you an edge list "edges" and number of nodes "n"

    The nodes will be in consecutive order starting from either 0 or 1.
    """
    def dfs(index):
        # Constraint - visited
        if visited[index] == 1:
            return

        # Process - mark current index as visited
        visited[index] = 1
        print(index, end=" ")

        # Get all the neighbors of this node
        for neighbor in adj.get(index):
            dfs(neighbor)

    # Convert edge list to adjacency list
    adj = dict()
    for i in range(n):  # Add node.val (key) with empty neighbors (val)
        adj[i] = []
    for i in range(len(edges)):  # Add edges into neighbors
        adj.get(edges[i][0]).append(edges[i][1])
        adj.get(edges[i][1]).append(edges[i][0])

    # Create a visited array, where 0 = unvisited and 1 = visited
    visited = [0] * n

    # Perform DFS on desired start point. In this case we start at index 0.
    dfs(0)


if __name__ == '__main__':

    # Adjacency List
    print("\nDFS Recursive Graph Adj List")
    n = 6  # n -> Number of nodes
    edges = [[0, 1], [1, 2], [1, 3], [2, 4], [4, 5]]  # Edge List
    traverse_edge_list(n, edges)