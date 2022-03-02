class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def buildGraph(isConnected):
            value_to_node = {} # map to track nodes
            
            for i in range(len(isConnected)):
                if i not in value_to_node:
                    prev = Node(i)
                    value_to_node[i] = prev
                else:
                    prev = value_to_node[i]

                for j in range(i+1, len(isConnected)):
                    if j not in value_to_node:
                        curr = Node(j)
                        value_to_node[j] = curr
                    else:
                        curr = value_to_node[j]

                    if isConnected[i][j] == 1:
                        prev.neighbors.append(curr)
                        curr.neighbors.append(prev)
        
            return value_to_node
        
        def dfs(current):
            if current in visited:
                return
            
            visited.add(current)
            
            for neighbor in current.neighbors:
                dfs(neighbor)
            
            return
        
        value_to_node = buildGraph(isConnected)
        result = 0
        visited = set()
        for i in range(len(isConnected)):
            node = value_to_node[i]
            if node in visited:
                continue
            dfs(node)
            result += 1
        return result