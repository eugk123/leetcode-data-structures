"""
https://leetcode.com/problems/maximum-product-subarray/
https://www.youtube.com/watch?v=vtJvbRlHqTA

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Examples:
    Input:          Output:
1)  [2,3,-2,4]      6
2)  [-2,0,-1]       0
3)  [2,3,-2,-4]     48

Explanation:
1)  [2,3] has the largest product 6.
2)  The result cannot be 2, because [-2,-1] is not a subarray.
3)  Two negative numbers = positive

:type nums: List[int]
:rtype: ans: int
"""
from typing import List
class Solution:
    """
    Complexity:
    Time: O(n) - traversing the array once
    Space: O(1) - Only a 5 variables that are updated and replaced over each iteration
    """
    def maximumProductSubarray(self, nums: List[int]) -> int:
        prev_max_product = prev_min_product = ans = nums[0]  # Initialize everything to the first element
        for num in nums[1:]:  # Iterate through the rest of the array. Maintain the current max and min products.
            curr_max_product = max(prev_max_product * num, prev_min_product * num, num)
            curr_min_product = min(prev_max_product * num, prev_min_product * num, num)  # We want to maintain the min product because two negative multipliers = positive
            ans = max(ans, curr_max_product)
            prev_max_product = curr_max_product  # Update previous products
            prev_min_product = curr_min_product
        return ans

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2, 4, 1, -3, 5, 2, -1]
    print(Solution().maximumProductSubarray(nums))