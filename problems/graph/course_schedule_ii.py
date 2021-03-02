"""
https://leetcode.com/problems/course-schedule-ii/
"""
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Directed Graph - Find Cycle
        https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation
        """
        def dfs(node):
            # If neighbor is visited, no cycle. Continue.
            if visited[node] == 1:
                return

            # If neighbor is in visiting state, then we have a cycle
            if visited[node] == -1:
                return True

            visited[node] = -1

            for neighbor in adj.get(node):
                if dfs(neighbor):
                    return True

            # Append deepest node and set to visited post recursion.
            res.append(node)
            visited[node] = 1

            return

        # Base cases.
        if numCourses == 1 and prerequisites == []:
            return [0]

        # Initialize adj list and res
        res = []
        adj = dict()
        for i in range(numCourses):
            adj[i] = []
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])

        # visited array can be of 3 forms:
        # 0 - unvisited, -1 - visiting, 1 - visited
        visited = [0] * numCourses

        # Iterate through each node because we could have multiple components.
        for node in adj:
            if dfs(node):  # If there is a cycle, return []
                return []
        return res  # Otherwise, return res

if __name__ == '__main__':
    print(Solution().findOrder(numCourses = 6, prerequisites = [[2,0],[3,0],[4,0],[5,4],[5,3],[1,5]]))
    # print(Solution().findOrder(numCourses=3, prerequisites=[[0,1],[1,2]]))