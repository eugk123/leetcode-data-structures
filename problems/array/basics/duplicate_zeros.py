"""
https://leetcode.com/problems/duplicate-zeros/
"""
from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Looking for optimal space O(1) and time O(n).
        # Do modifications on input array IN PLACE.

        # First pass - two pointer - left and right end - count zeroes
        # Iterate with left pointer. If zero is found, set right as None, and traverse.
        # End when left == right.

        # Example:
        #          [0 1 0 2 3]
        # i = 0 -> [0 1 0 2 -]
        # i = 2 -> [0 1 0 - -]
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] == 0:
                arr[right] = None
                right -= 1
            left += 1

        # Edge case, if the first number that shows up is zero, only copy it over once.
        # Store left pointer

        # Example:
        #          [0 1 0 2 3]
        # i = 2 -> [0 1 0 0 0]
        # i = 1 -> [0 1 1 0 0]
        # i = 0 -> [0 0 1 0 0]
        last_index = left
        if arr[left] == 0:
            is_first_zero = True
        else:
            is_first_zero = False

        # Second pass - two pointer - both at end - duplicate zeroes by populating backwards
        second = len(arr) - 1
        for first in reversed(range(len(arr))):
            # Edge Case -> first zero at end, copy only once.
            if is_first_zero == True and arr[first] == 0:
                arr[second] = arr[first]
                second -= 1
                is_first_zero = False
                continue
            if arr[first] == None:
                continue
            if arr[first] == 0:
                arr[second] = arr[first]
                second -= 1
            arr[second] = arr[first]
            second -= 1

