"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=7Q1uylXOatU&t=143s

        Sliding Window
        """
        curr_sum = left = 0

        length = 99999
        for right in range(len(nums)):
            curr_sum = curr_sum + nums[right]

            while curr_sum >= s:
                # Get the difference between pointers for length
                length = min(length, right - left + 1)

                # Update the current sum by subtracting the left element.
                curr_sum = curr_sum - nums[left]
                left += 1
        return length

if __name__ == '__main__':
    print(Solution().minSubArrayLen(s=4, nums=[1,2,1,4,3]))
