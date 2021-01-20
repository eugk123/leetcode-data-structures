"""
https://leetcode.com/problems/maximum-subarray/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

Examples:
    Input:                      Output:
1)  [-2,1,-3,4,-1,2,1,-5,4]     6
Explanation:
1)  [4,-1,2,1] has the largest sum = 6.

Complexity:
Time: O(n)
Space: O(1) - no additional resources created.
"""
from typing import List
import math
class Solution:
    """
    https://www.youtube.com/watch?v=u7YMFRUFqe0&t=372s

    Use Sliding Window
    """
    def maximumSubarray(self, nums: List[int]) -> int:
        left = currSum = 0
        maxSum = -math.inf
        for right in range(len(nums)):
            currSum = currSum + nums[right]
            maxSum = max(maxSum, currSum)
            while currSum < 0:
                currSum = currSum - nums[left]
                left += 1

        return maxSum

    def maximumSubarrayGreedy(self, nums: List[int]) -> int:
        if not nums:  # Base Case. If empty, return 0
            return 0
        curSum = maxSum = nums[0]  # Initialize everything w/ first element
        for num in nums[1:]:  # Iterate through index 1 onwards:
            curSum = max(num, curSum + num)  # We're looking at either taking the max of the new number of the currSum + new number
            maxSum = max(curSum, maxSum)  # We then check to see if maxSum is still the max or should be replaced with curSum
        return maxSum

    def maximumSubArray_BruteForce(self, nums):
        """
        Brute Force Solution.
        Time: O(n^2)
        """
        sums = []
        for j in range(0, len(nums)-1):
            sum_value = 0
            for i in range(j, len(nums)):
                sum_value = sum_value + nums[i]
                sums.append(sum_value)
        return max(sums)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2, -4, 3, 5, -2, -5, -1, 2, 1, -2, 3, -1, 1, 6, -7]
    print("O(n) Sliding Window w/ O(1) space: {}".format(Solution().maximumSubarray(nums)))
    print("O(n) Greedy w/ O(1) space: {}".format(Solution().maximumSubarrayGreedy(nums)))
    print("O(n^2) Brute Force: {}".format(Solution().maximumSubArray_BruteForce(nums)))
