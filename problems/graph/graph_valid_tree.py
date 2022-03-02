from typing import List
class Solution:
    """
    Detect Cycle in Undirected Graph

    Time O(N + E)
    The adjacency list is a list of length N, with inner lists with lengths that add to a total of E. 
    This gives a total of O(N + E) space

    Space O(N + E) 
    The adjacency list is a list of length N, with inner lists with lengths that add to a total of E. 
    This gives a total of O(N + E) space
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
                            
        def dfs(current, parent):
            if current in visited:
                return True
            
            visited.add(current)
            
            for neighbor in adj.get(current):
                if neighbor == parent:
                    continue
                    
                if neighbor in visited:
                    return False
                
                if not dfs(neighbor, current):
                    return False
                
            return True
        
        visited = set()
        
        # return true if no cycles detected and entire graph has been reached
        return dfs(0, -1) and len(visited) == n
        
    def validTreeBFS(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        def bfs(source):
            queue = deque([source])
            queue_set = set()
            queue_set.add(source)
            
            while queue:
                curr = queue.popleft()
                queue_set.remove(curr)

                visited.add(curr)
                
                for nei in adj.get(curr):
                    
                    if nei in queue_set:
                        return False
                    
                    if nei in visited:
                        continue
                    
                    
                    queue_set.add(nei)
                    queue.append(nei)
                    
            return True
                
        visited = set()
        if not bfs(0):
            return False
        
        if len(visited) != n:
            return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty edge list, only True when n == 1.
        if not edges and n == 1:
            return True

        # So 5 nodes should have exactly 4 edges.
        # Or N node should have N-1 edges.
        # This means we can't have extra edges (cycle)
        if n != len(edges) + 1:
            return False

        # Build adj list
        adj = {}
        for edge in edges:
            if not adj.get(edge[0]):
                adj[edge[0]] = []
            if not adj.get(edge[1]):
                adj[edge[1]] = []
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # If one of the nodes are missing, then return False
        for i in range(n):
            if i not in adj:
                return False

        # If fully connected, return True.
        def dfs(index):
            if visited[index] == 1:
                return
            visited[index] = 1
            for nei in adj.get(index):
                if visited[nei] == 0:
                    dfs(nei)

        visited = [0] * n
        dfs(0)

        # This tells if there are unvisited components, then we have multiple components.
        if 0 in visited:
            return False
        return True


if __name__ == '__main__':
    print(Solution().validTree(n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]))