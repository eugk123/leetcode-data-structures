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
        def dfs(current, index):
            # Constraint - repeat letters are found
            if len(set(current)) != len(list(current)):
                return

            # Process
            self.result = max(self.result, len(current))

            # Constraint - end is reached
            if index == len(arr):
                return

            # Traverse to each neighbor to the right.
            for i in range(index, len(arr)):
                dfs(current + arr[i], i + 1)

            return

        self.result = 0

        # Start empty that way you can start at all nodes.
        dfs("", 0)

        return self.result

if __name__ == '__main__':
    print(Solution().maxLength(arr=['aa','nvf','abaaacd','rqs','dgh','jqp']))