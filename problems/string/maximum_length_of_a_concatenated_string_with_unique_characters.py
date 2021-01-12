'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        https://www.youtube.com/watch?v=pD3cHFNyW2I

        Use a Set to store each char individually, we can use the length of the set to compare with the word and know
        whether or not the word has duplicates

        You want to try doing every combination. So use backtracking.

        Time Complexity: O(2^n) - 1 top level recursive call. 2 different calls for every word. So that's O(2n) = O(n)
        Space Complexity: O(2^n) - Since we have N words, we will go N stack frames deep into the recursion.
        """
        result = [0]

        self.maxUniqueDfs(arr, 0, "", result)

        return result[0]

    def checkDuplicateChars(self, s):
        if len(set(s)) < len(s):  # Duplicate Characters
            return -1
        return len(s)  # Unique Characters

    def maxUniqueDfs(self, arr, index, current, result):
        # Base Case: If repeating characters exist
        if self.checkDuplicateChars(current) == -1:
            return

        # Base Case: End of array with existing result (Update result with best answer)
        if index == len(arr) and self.checkDuplicateChars(current) > result[0]:
            result[0] = len(current)
            return

        # Base Case: End of array
        if index == len(arr):
            return

        # Perform recursion
        # Send search parties to every index on the right from current index.
        self.maxUniqueDfs(arr, index + 1, current, result)
        self.maxUniqueDfs(arr, index + 1, current + arr[index], result)

if __name__ == '__main__':
    print(Solution().maxLength(arr=['aa','nvf','abc','abaaacd']))



# from typing import List
# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         def checkDuplicateChars(s):
#             if len(set(s)) < len(s):  # Duplicate Characters
#                 return -1
#             return len(s)  # Unique Characters
#
#         def maxUniqueDfs(index, current):
#             # Base Case: End of array with existing result (Update result with best answer)
#             print(index, len(arr), checkDuplicateChars(current), result[0])
#             if index == len(arr) and checkDuplicateChars(current) > result[0]:
#                 print("ABC")
#                 result[0] = max(len(current), result[0])
#                 return
#
#             # Base Case: End of array
#             if index == len(arr):
#                 return
#             print(index, current, len(current), result)
#             # Perform recursion on each and every index with sending search parties to the right.
#             # ex: ['a','b','c'] -> 'a', 'ab', 'abc', 'b', 'bc', 'c'
#             for index in range(index, len(arr)):
#                 # self.maxUniqueDfs(arr, index + 1, current, result)  # Taking the string at the index position
#                 maxUniqueDfs(index + 1, current + arr[index])  #
#
#         result = [0]
#
#         maxUniqueDfs(0, "")
#
#         return result[0]
#
#
#
# if __name__ == '__main__':
#     print(Solution().maxLength(arr=["cha","r","act","ers"]))