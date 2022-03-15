"""
https://leetcode.com/problems/edit-distance/
"""
class Solution:
    """
    Top-down Memo 2D

    Minimum number of moves. 
    - Out of bounds return: 0
    - End of array 1 return: remaining number of operations when word2 end is reached
    - End of array 2 return: remaining number of operations when word1 end is reached
    - End return (same letters): return current number of operations
    - End return (different letters): return 1(plus 1 operation) + current number of operations

    https://www.youtube.com/watch?v=AuYujVj646
    """
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Top-Down DP - DFS without Memoization

        Time and Space Complexity: O(n*m) which is effectively the size of the cache
        """
        # The key trick here is to find all boundary and possible cases without having to make modifications to the current words.
        # All you need to do is move the indices based on what you are doing
        # You also want to start at the far left and work towards the right.
        def dfs(i, j):
            # Return cached result if it exists
            if (i, j) in memo:
                return memo.get((i,j))
            
            # end of both reached, no more operations needed
            if i == len(word1) and j == len(word2):
                return 0

            # end of word1 reached, then word1 has l1-j removal operations needed to meet word1 size
            if i == len(word1):
                return len(word2) - j
            
            # end of word2 reached, then word2 has l2-i removal operations needed to meet word2 size
            if j == len(word2): 
                return len(word1) - i
            
            # same letter - 1 path, don't count
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1) # skip both: move both indices

            # not same letter - 3 paths, count +1
            else:
                a = dfs(i + 1, j + 1)   # replace, move both indices
                b = dfs(i, j + 1)       # insert, move j only
                c = dfs(i + 1, j)       # delete, move i only
                memo[(i, j)] = 1 + min(a,b,c)   # cache result
                
                return 1 + min(a, b, c)   # we're taking minimum result at every path
            
        memo = {}
        return dfs(0, 0)

    def minDistance_TLE(self, word1: str, word2: str) -> int:
        """
        DFS without Memoization

        Time and Space Complexity: O(3^n) due to the redundant recursive 3x calls
        """
        # The key trick here is to find all boundary and possible cases without having to make modifications to the current words.
        # All you need to do is move the indices based on what you are doing
        # You also want to start at the far left and work towards the right.
        def dfs(i, j):
            # end of both reached, no more operations needed
            if i == len(word1) and j == len(word2):
                return 0

            # end of word1 reached, then word1 has l1-j removal operations needed to meet word1 size
            if i == len(word1):
                return len(word2) - j
            
            # end of word2 reached, then word2 has l2-i removal operations needed to meet word2 size
            if j == len(word2): 
                return len(word1) - i
            
            # same letter - 1 path, don't count
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1) # skip both: move both indices

            # not same letter - 3 paths, count +1
            else:
                a = dfs(i + 1, j + 1)   # replace, move both indices
                b = dfs(i, j + 1)       # insert, move j only
                c = dfs(i + 1, j)       # delete, move i only
                
                return 1 + min(a, b, c)   # we're taking minimum result at every path
            
        return dfs(0, 0)