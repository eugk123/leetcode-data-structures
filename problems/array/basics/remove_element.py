"""
https://leetcode.com/problems/remove-element/
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        for i in range(len(nums)):
            # Count everytime you match targeted value
            if nums[i] == val:
                count += 1

            # Use that count and subtract from current index to replace that element with current element
            elif nums[i] != val:
                nums[i - count] = nums[i]

        while count > 0:
            nums.pop()
            count -= 1

        print(nums)
        print(count)

        return