"""
https://leetcode.com/problems/sort-colors
"""
from typing import List
class Solution:
    """
    Two Pass Two Pointer - Linear Time Constant Space

    Pass twice. First pass, swap when target == 0. Second pass, swap when target == 1.

    On second pass, continue off of left pointer
    Time O(n)
    Space O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swapTarget(target, nums):
            for i in range(self.left, len(nums)):
                if nums[i] == target:
                    tmp = nums[self.left]
                    nums[self.left] = nums[i]
                    nums[i] = tmp
                    self.left += 1
        self.left = 0
        swapTarget(0, nums)
        swapTarget(1, nums)
