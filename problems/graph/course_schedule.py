"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        https://www.youtube.com/watch?v=a4hXpeHZ_-c&t=506s

        Cycle Detection:
        Keep track of whether or not the node has been visited with an array.
        The array contains three numbers: (0 = Unvisited, 1 = Visited, -1 = Visiting).
        Once the entire graph has been visited or if a cycle is detected when a traversing back to a “visiting” node, the recursion ends.
        """
        # Setup Adjacency Matrix based on numCourses and edges
        adj = dict()
        for i in range(numCourses):
            adj[i] = []
        for edge in prerequisites:
            adj.get(edge[0]).append(edge[1])

        # Unvisited = 0 -> Node is unvisited
        # Visiting = -1 -> Currently visiting this node
        # Visited = 1   -> Previously visited this node on a previous travesal
        visited = [0] * numCourses

        for i in range(numCourses):
            return self.dfs(adj, i, visited)

        # Otherwise, return True
        return True

    def dfs(self, adj, index, visited):
        # Cycle detection when neighboring node is marked as visiting during traversal.
        if visited[index] == -1:
            return False

        # Immediately set to visiting
        visited[index] = -1

        for index in adj.get(index):
            self.dfs(adj, index, visited)

            # If cycle is found, return False
            if self.dfs(adj, index, visited) is False:
                return False

        visited[index] = 1
        return True

if __name__ == '__main__':
    print(Solution().canFinish(numCourses=3, prerequisites=[[0,1],[1,2],[2,0]]))