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
    def possibleBipartition(self, N, dislikes):
        def dfs(index, prev_group):
            print(index, prev_group, visited[index - 1])

            if visited[index - 1] == prev_group:
                return False

            # Group A = 1, Group B = -1
            if visited[index - 1] == 1 or visited[index - 1] == -1:
                return

            # Alternate Groups Every Traversal, Starting point (else) set to 1
            if prev_group == 1:
                visited[index - 1] = -1
            elif prev_group == -1:
                visited[index - 1] = 1
            else:
                # You can choose either 1 or -1.
                visited[index - 1] = 1

            for nei in adj.get(index):
                prev = visited[index - 1]
                if dfs(nei, prev) is False:
                    return False

            return

        adj = {}
        # Range 1 to N + 1 because first index is 1
        for i in range(1, N + 1):
            adj[i] = []

        for edge in dislikes:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [0] * N

        # Can have multiple components
        # First index = 1
        for i in range(1, N + 1):
            prev = None  # There is no previous, so set to None
            if dfs(i, prev) is False:
                return False

        return True

if __name__ == '__main__':
    # print(Solution().possibleBipartition(5, [[0, 1], [2, 3], [3, 4], [4, 2]]))
    print(Solution().possibleBipartition(5, [[1, 2], [3, 4], [4, 5], [5, 3]]))