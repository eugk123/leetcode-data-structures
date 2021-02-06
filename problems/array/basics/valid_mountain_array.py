"""
https://leetcode.com/problems/valid-mountain-array/
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # This only works if len > 2
        if len(arr) <= 2:
            return False

        # Need to verify that at least the first two indices are increasing order.
        if arr[1] < arr[0]:
            return False

        past_peak = False
        for i in range(1, len(arr)):
            # If duplicate, return false
            if arr[i] == arr[i - 1]:
                return False

            # First find the peak which should be the first inflection
            if not past_peak and arr[i] < arr[i - 1]:
                past_peak = True

            # Now if it ever starts increasing again, then you know it's not a perfect mountain
            if past_peak and arr[i] > arr[i - 1]:
                return False

        if past_peak:
            return True
        else:
            return False