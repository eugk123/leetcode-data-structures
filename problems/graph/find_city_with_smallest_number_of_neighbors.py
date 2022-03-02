"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""
from collections import heapq
class Solution:
    """
    Djikstra's Algorithm

    Time Complexity: O(V*E*logV)
    Vertix = V, Edge = E. At every vertex, the time complexity is O(E * log V), log v is due to heappush. Since we run this at every vertex, the total time complexity is V * (E * log V)
    Space Complexity: O(N) - size of recursion stack / size of map.

    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # Buld adjacency list - include nodes without connectinos
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            if not adj.get(edge[0]):
                adj[edge[0]] = []
            if not adj.get(edge[1]):
                adj[edge[1]] = []
            adj[edge[0]].append((edge[1],edge[2]))
            adj[edge[1]].append((edge[0],edge[2]))

        # Dijkstra's algorithm - BFS w/ Heap consisting of (cost, node_value)
        def bfs_dijkstra(current):
            source = current
            # load heap with (net_cost, city) for correct min heap action!
            min_heap = [(0, current)]  # we are sorting on cost, so cost must be first
            visited = set()

            while min_heap:
                net_cost, current = heapq.heappop(min_heap)
                
                # Constraint - Visited - Skip
                if current in visited:
                    continue

                # Constraint - Cost Exceeded - Break
                if net_cost > distanceThreshold:
                    break
                
                # Add to visited.
                visited.add(current)

                # Traverse neighbors
                for nei, cost in adj[current]:
                    # If visited, skip
                    if nei in visited:
                        continue
                    
                    # Add to heap - (total cost, node_value)
                    heapq.heappush(min_heap, (net_cost + cost, nei))
            
            # Updating minimum
            if len(visited) <= self.minimum_visited_cities:
                self.minimum_visited_cities = len(visited)
                self.result = source

        # Run dijkstra's at every node
        self.minimum_visited_cities = float("inf")
        self.result = None
        for current in range(n):
            bfs_dijkstra(current)
        
        return self.result