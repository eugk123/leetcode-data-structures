"""
https://leetcode.com/problems/longest-repeating-substring/
"""
class Solution:
    """
    https://www.youtube.com/watch?v=Tf_mD59DLf0
    """
    def longestRepeatingSubstring(self, S: str) -> int:
        """
        Binary Search w/ Hash Map)

        The trick is to use a hashmap to check if the string already exists in the map.
        If it already exists in the map, update the max length of the substring.

        Time - O(n^2)
        Space - O(n^2)
        """


    def longestRepeatingSubstringBruteForce(self, S: str) -> int:
        """
        Brute Force Approach w/ Hash Map (Accepted)

        The trick is to use a hashmap to check if the string already exists in the map.
        If it already exists in the map, update the max length of the substring.

        Time - O(n^2)
        Space - O(n^2)
        """

        check = set()
        max_length = 0
        # "abcd"
        # i = 0, j = 1 - "a"
        # i = 0, j = 2 - "ab"
        # i = 0, j = 3 - "abc"
        # ...
        # i = 3, j = 4 - "c"
        # i = 3, j = 5 - "cd"
        # i = 4, j = 5 - "d"
        for i in range(len(S)):

            # S[0:0] = "", but S[0:1] = "a", so we need to add +1 to the start and end range for j.
            for j in range(i + 1, len(S) + 1):
                if S[i:j] not in check:
                    check.add(S[i:j])
                else:
                    max_length = max(len(S[i:j]), max_length)

        return max_length