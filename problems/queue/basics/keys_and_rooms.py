"""
https://leetcode.com/problems/keys-and-rooms/
"""
from typing import List
class Solution:
    """
    DFS using Adjacency List. Similar to Course Schedule.

    Notice we can have cycles. So for visited, you'll have the options for 0-unvisited, -1-visiting, and 1-visited.
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(index):
            if visited[index] == 1:
                return

            # Unvisited -> Visiting
            if visited[index] == 0:
                visited[index] = -1

            # Visiting -> Visited
            else:
                visited[index] = 1

            for neighbor in adj.get(index):
                dfs(neighbor)
            return

        adj = {}
        for i in range(len(rooms)):
            adj[i] = rooms[i]

        visited = [0] * len(rooms)
        dfs(0)

        if 0 in visited:
            return False
        else:
            return True