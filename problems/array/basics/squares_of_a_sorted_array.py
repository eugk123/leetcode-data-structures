"""
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
"""
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        O(n) time using 1 pass 2 pointer solution.
        """
        # The optimal algorithm is to start left and right pointers at the end.
        # Compare the absolute values, which ever is greater, replace value in that pointer.

        # Remember, replacing an existing element in an array is O(1). So initialize your result first.
        # Even though appending at the end is O(1) time, inserting is O(n) time.
        res = [0] * len(nums)

        left = 0
        i = right = len(nums) - 1
        while i > -1:

            # Compare ends. If right is greater, append right to end
            if abs(nums[left]) <= abs(nums[right]):
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
            i -= 1
        return res