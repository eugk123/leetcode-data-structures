"""
https://leetcode.com/problems/possible-bipartition/

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.


"""
class Solution:
    """
    https://www.youtube.com/watch?v=a4hXpeHZ_-c&t=950s

    Bipartite Graph:

    Keep track of whether or not the node has been visited with an array.
    The array contains three numbers: (0 = Unvisited, 1 = Group A, -1 = Group B).
    Once the entire graph has been visited or if two node of the same group are next to each other, the recursion ends.
    """
    def possibleBipartition(self, n, dislikes):
        # Build adjacency list
        adj = dict()  # Initialize map
        for i in range(0, n): adj[i] = []  # Fill in Keys with empty lists
        for edge in dislikes:
            adj.get(edge[0]-1).append(edge[1]-1)
            adj.get(edge[1]-1).append(edge[0]-1)

        # Perform DFS
        visited = [0] * n

        # We search through every node in case of multiple components e.g. [[1,2],[3,4],[4,5],[3,5]]
        for index in range(0, n):
            # If dfs finds two neighbors with same grouping, then return false
            if visited[index] == 0 and self.dfs(adj, visited, index, 99) is False:
                return False
        return True


    def dfs(self, adj, visited, index, previous):
        # Closure Condition
        if previous == visited[index]:
            return False
        if visited[index] == -1 or visited[index] == 1:
            return True

        # Alternate Groups Every Traversal, Starting point (else) set to 1
        if previous == 1:
            visited[index] = -1
        elif previous == -1:
            visited[index] = 1
        else:
            visited[index] = 1

        for neighbor_index in adj.get(index):
            previous = visited[index]
            if self.dfs(adj, visited, neighbor_index, previous) is False:
                return False
        return True

if __name__ == '__main__':
    # print(Solution().possibleBipartition(5, [[0, 1], [2, 3], [3, 4], [4, 2]]))
    print(Solution().possibleBipartition(5, [[1, 2], [3, 4], [4, 5], [5, 3]]))