class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val  # Node Value
        self.neighbors = neighbors if neighbors is not None else []  # List of adjecent node
        self.graph_dict = dict()