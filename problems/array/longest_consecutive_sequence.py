"""
https://leetcode.com/problems/longest-consecutive-
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:

            # This condition will skip all numbers until a possible starting point is found.
            # For example, if we have [5,4,3,2,1], with this condition, it will only start at last index with value 1.
            # Without this condition, we would run through this loop for every single index.
            if num - 1 not in nums:

                # Reset count to 1
                count = 1

                # Set current
                current = num

                # Since we're using a hashset, the lookup of next consecutive number is O(1)
                while current + 1 in nums:
                    # Iterate current and count
                    count += 1
                    current += 1

                # Take the max every iteration!
                max_count = max(count, max_count)

        return max_count