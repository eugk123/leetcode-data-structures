"""
https://leetcode.com/problems/reverse-string/
"""
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        O(1) constant space solution
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap
            temp = s[right]
            s[right] = s[left]
            s[left] = temp

            # Traverse
            right -= 1
            left += 1

    def reverseStringRecursive(self, s: List[str]) -> None:
        """
        Try recursive method
        """
        def helper(s, left, right):
            # Base Case
            if left >= right:
                return

            temp = s[right]
            s[right] = s[left]
            s[left] = temp

            # Recurrence relationship
            helper(s, left + 1, right - 1)

        helper(s, 0, len(s) - 1)
        return s
