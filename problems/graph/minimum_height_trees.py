"""
https://leetcode.com/problems/minimum-height-trees/

This problem is very difficult to illustrate in text. Please refer to the link above.

Note that the solution returns a List because there can be 2 root node.
"""
from typing import List
class Solution:
    """
    First collect all leaf nodes as initial queue. 
    Level-order BFS Traversal.
                        leaves
    1---0---2           [1,2,5] 6
        |
        3---4---5
    
        0---3---4       [0,4]   3
                        
            3           [3]     1
            
                        leaves  remaining
    0---1---2---4---6   [0,5,6] 7
        |
        3---5
        
        1---2---4       [4,3]   4
        |
        3
        
        1---2  result = [1,2]   2  

    Time and Space O(N) where N is the number of nodes (or vertices)
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        if len(edges) == 1:
            return [0,1]
        
        # Notice each node in adjacency list uses a set. This is crucial for finding the next inner leaf.
        adj = {}
        for i in range(n):
            adj[i] = set()
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
            
        leaves = []
        for key in adj:
            if len(adj.get(key)) == 1:
                leaves.append(key)
        
        # keep iterating until there are two nodes left
        # if performing level by level updates, it should result in remaining one or two centroids!        
        visited = set()
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)  # subtract total from # of leaves that will be detached
            new_leaves = []
            # level-order, we strip leaves until empty and populate new_leaves
            while leaves:
                parent = leaves.pop()
                
                # for each leaf, we want to find the next inner leaf by iterating each neighbor
                for nei in adj.get(parent):

                    # we want to detach the inner node from outer leaf to create a new leaf node
                    # we cannot skip this process. must be done on every node!
                    adj.get(nei).remove(parent)
                    # now we can skip if visited
                    if nei in visited:
                        continue
                    
                    if len(adj.get(nei)) == 1:
                        # add to visited
                        visited.add(nei)

                        # add to next level, only if it's a leaf node
                        new_leaves.append(nei)

            # update next level
            leaves = new_leaves
        
        return leaves

if __name__ == '__main__':
    print(Solution().findMinHeightTrees(n=6, edges=[[0,1],[1,2],[1,3],[1,4],[4,5]]))