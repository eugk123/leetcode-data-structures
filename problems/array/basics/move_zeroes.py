"""
https://leetcode.com/problems/move-zeroes/submissions/
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # As you traverse, count zeroes.
        count = 0
        for i in range(len(nums)):
            # Count zeroes
            if nums[i] == 0:
                count += 1

            # When num is not zero, then update index - count with current value and update current with 0.
            # You want to make sure you're updating the current index to 0 ONLY when there are zeroes.
            elif count > 0:
                nums[i - count] = nums[i]
                nums[i] = 0
