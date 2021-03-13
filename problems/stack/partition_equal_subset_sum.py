"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
from typing import List
class Solution:
    """
    DFS w/ Memoization

    Time complexity is O(n*m) where n is length of memoization array and m is subsetSum (total/2) which is effectively the
    size of the memo.
    Space complexity is O(n*m) as well
    """
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(current, index):
            # Check memo
            if current in memo:
                return memo.get(current)

            # Looking for current to sum up to target
            if current == target:
                return True

            # If current goes beyond target, we know it's False
            if current > target:
                return False

            # Out of bounds - Make sure to have this after checking against target because nums[i] is using index-1.
            if index == len(nums):
                return False

            memo[current] = False

            # Traverse
            for i in range(index, len(nums)):
                if dfs(current + nums[i], i + 1):
                    return True
            return False

        # First pass, get total sum
        total = sum(nums)

        # If total sum is odd, then return False, because we're not gonna have partitioned sums equal to each other
        if total % 2 == 1:
            return False

        # Otherwise, get target = total/2
        target = total / 2

        memo = {}
        return dfs(0, 0)

    def canPartition_TLE(self, nums: List[int]) -> bool:
        """
        TLE due to missing memoization array/map.

        Worst case scenario is time = O(2^n).
        """
        def dfs(current, index):

            # Looking for current to sum up to target
            if current == target:
                return True

            # If current goes beyond target, we know it's False
            if current > target:
                return False

            # Out of bounds - Make sure to have this after checking against target because nums[i] is using index-1.
            if index == len(nums):
                return False

            # Traverse
            for i in range(index, len(nums)):
                if dfs(current + nums[i], i + 1):
                    return True

        # First pass, get total sum
        total = 0
        for num in nums:
            total = total + num

        # If total sum is odd, then return False, because we're not gonna have partitioned sums equal to each other
        if total % 2 == 1:
            return False

        # Otherwise, get target = total/2
        target = total / 2

        return dfs(0, 0)
