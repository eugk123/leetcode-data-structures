"""
https://leetcode.com/problems/find-peak-element/
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:

            mid = left + (right - left) // 2

            # Somewhere in the middle there is a peak
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid + 1] and nums[mid - 1] < nums[mid]:
                    return mid

            # Far right there is a peak if shaped like: /
            if mid == len(nums) - 2:
                if nums[mid] < nums[len(nums) - 1]:
                    return len(nums) - 1

            # Far left there is a peak if shaped like: \
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
