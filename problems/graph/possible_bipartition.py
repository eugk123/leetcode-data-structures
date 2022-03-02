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
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for edge in dislikes:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(current, previous_visited_value):            
            # Before returning on visited,
            # Check if current and previous are same type. If so, not a bipartite graph!
            if previous_visited_value == visited[current - 1]:
                return False
            
            # If visited, return
            if visited[current - 1] != 0:
                return True            

            # If previous visited is 1, then we switch current visited to -1
            if previous_visited_value == 1:
                visited[current - 1] = -1
            else:
                visited[current - 1] = 1
            
            for nei in adj.get(current):
                # Update previous visited value
                previous_visited_value = visited[current - 1]
                if not dfs(nei, previous_visited_value):
                    return False
            return True
        
        visited = [0] * n

        # We want to check all components
        for i in range(1, n + 1):
            if not dfs(i, None):
                return False
        return True

if __name__ == '__main__':
    # print(Solution().possibleBipartition(5, [[0, 1], [2, 3], [3, 4], [4, 2]]))
    print(Solution().possibleBipartition(5, [[1, 2], [3, 4], [4, 5], [5, 3]]))