"""
https://leetcode.com/problems/edit-distance/
"""
class Solution:
    """
    https://www.youtube.com/watch?v=AuYujVj646
    """
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Top-Down DP - DFS without Memoization

        Time and Space Complexity: O(n*m) which is effectively the size of the cache
        """
        l1 = len(word1)
        l2 = len(word2)

        # The key trick here is to find all boundary and possible cases without having to make modifications to the current words.
        # All you need to do is move the indices based on what you are doing
        # You also want to start at the far left and work towards the right.
        def recur(i1: int, i2: int) -> int:
            # Return cached result if it exists
            if memo.get((i1, i2)):
                return memo[(i1, i2)]

            # BC: End is reached for both words, then no more operations needed.
            if i1 == l1 and i2 == l2: return 0

            # BC: word1 end is reached, then word2 has l2-i2 removal operations needed to meet word1 size
            if i1 == l1: return l2 - i2

            # BC: word2 end is reached, then word1 has l1-i1 removal operations needed to meet word1 size
            if i2 == l2: return l1 - i1

            # Same letter at current indices. Traverse both to the right.
            if word1[i1] == word2[i2]:
                memo[(i1, i2)] = recur(i1 + 1, i2 + 1)

            # Other possible cases
            else:
                # Insert at i1, so move i2 to the right
                r1 = recur(i1, i2 + 1)

                # Delete at i1, so move i1 to the right only
                # r2 = recur(i1 + 1, i2)

                # Replace at i1, so move both i1 and i2 to the right
                # r3 = recur(i1 + 1, i2 + 1)
                memo[(i1, i2)] = 1 + r1

            return memo[(i1, i2)]

        # Memo map will contain value->indices to key->min_count
        memo = {}
        return recur(0, 0)

    def minDistance_TLE(self, word1: str, word2: str) -> int:
        """
        DFS without Memoization

        Time and Space Complexity: O(3^n) due to the redundant recursive 3x calls
        """
        l1 = len(word1)
        l2 = len(word2)

        # The key trick here is to find all boundary and possible cases without having to make modifications to the current words.
        # All you need to do is move the indices based on what you are doing
        # You also want to start at the far left and work towards the right.
        def recur(i1: int, i2: int) -> int:
            # BC: End is reached for both words, then no more operations needed.
            if i1 == l1 and i2 == l2: return 0

            # BC: word1 end is reached, then word2 has l2-i2 removal operations needed to meet word1 size
            if i1 == l1: return l2 - i2

            # BC: word2 end is reached, then word1 has l1-i1 removal operations needed to meet word1 size
            if i2 == l2: return l1 - i1

            # Same letter at current indices. Traverse both to the right.
            if word1[i1] == word2[i2]:
                return recur(i1 + 1, i2 + 1)

            # Other possible cases
            else:
                # Insert at i1, so move i2 to the right
                r1 = recur(i1, i2 + 1)

                # Delete at i1, so move i1 to the right only
                r2 = recur(i1 + 1, i2)

                # Replace at i1, so move both i1 and i2 to the right
                r3 = recur(i1 + 1, i2 + 1)
                return 1 + min(r1, r2, r3)

        return recur(0, 0)