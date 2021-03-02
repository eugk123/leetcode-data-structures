"""
https://leetcode.com/problems/house-robber/
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Bottom-up Memoization

        https://www.youtube.com/watch?v=73r3KWiEvyk&t

        example:
        idx.  0   1   2   3   4  ...
        nums [1,  2,  3,  1,  5  ...]
        opt1  x     | ?   ?   ?  ...
              1       4
        opt2      x     | ?   ?  ...
                  2       3
        max   1   2   4   4


        Recurrence relationship is
        dp(i) = dp(i-2) + nums[i]

        Since you can't rob adjacent houses, we can split the array into a subarray by skipping next index.
        """

        # Base cases for len of nums of 0, 1, and 2
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize memo array: key-nums_index, value-total_robbed
        dp = [0] * len(nums)

        # Base cases for i == 0 and i == 1
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Recurrence relationship
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]