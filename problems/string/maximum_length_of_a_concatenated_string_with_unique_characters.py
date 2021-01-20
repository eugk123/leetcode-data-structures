'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/419204/3-Solutions%3A-Backtracking-Recursive-and-DP-solutions-(With-Video-explanations)
        https://jamboard.google.com/d/1JMV60IvmTvqvcyf6dyc7bFG-VL0LDadsDia5xtwC8gk/viewer?f=0

        Use a Set to store each char individually, we can use the length of the set to compare with the word and know
        whether or not the word has duplicates

        You want to try doing every combination. So use backtracking.

        Time Complexity: O(2^n) - 1 top level recursive call. 2 different calls for every word. So that's O(2n) = O(n)
        Space Complexity: O(2^n) - Since we have N words, we will go N stack frames deep into the recursion.
        """
        self.result = 0  # Captures the length of the string. Will update when new max is found.

        # Send search parties on every index. To do so, we need to paramaterize index and current word.
        def dfs(index, current):
            # Return if duplicate letters is found
            if len(current) < len(set(current)):
                return

            # Return if end of array is reached
            if index == len(arr):
                return

            # Return if end of array is reached, but not duplicate, and result is greater than previous
            if len(current) == len(set(current)):
                self.result = max(self.result, len(current))

            # Call DFS at every index. To do so, we need to perform two recursions.
            # Recursively call using current word. This allows for starting at every index.
            # dfs(index + 1, current)

            # Recursively call using current word plus new word. This allows for combinations.
            for i in range(index, len(arr)):
                dfs(i + 1, current + arr[i])

        dfs(0, "")

        return self.result



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