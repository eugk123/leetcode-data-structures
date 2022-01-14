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
def maximumSubarray(nums: List[int]) -> int:    
    """
    https://www.youtube.com/watch?v=u7YMFRUFqe0&t=372s

    Use Sliding Window

    Every iteration, calculate sum
    -2 1 -3 4 -1 2 1 -5 4
    -2 slide
       1 -2 slide
            4  3 5 6  1 5
    MAX = 6
    """
    current_sum = 0
    max_sum = -math.inf
    l = 0   # Technically left pointer is not needed in this solution, but it's useful for visual
    
    for r in range(len(nums)):
        current_sum += nums[r]
        max_sum = max(current_sum, max_sum)
        
        # Slide left pointer (single left pointer update)
        # Satisfies when sum is negative, we slide left pointer up to the right pointer.       
        if current_sum <= 0:
            l = r + 1
            current_sum = 0
        
    return max_sum

def maximumSubArray_BruteForce(nums):
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
    print("O(n) Sliding Window w/ O(1) space: {}".format(maximumSubarray(nums)))
    print("O(n^2) Brute Force: {}".format(maximumSubArray_BruteForce(nums)))
