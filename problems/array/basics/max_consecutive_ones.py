"""
https://leetcode.com/problems/max-consecutive-ones/
"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                count = 0
            max_count = max(count, max_count)

        return max_count