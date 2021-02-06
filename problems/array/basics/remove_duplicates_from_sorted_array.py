"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)):
            # Count everytime you find duplicate between current and previous index
            if i > 0 and nums[i] == nums[i - 1]:
                count += 1

            # Use that count and subtract from current index to replace that element with current element
            elif i > 0 and nums[i] != nums[i - 1]:
                nums[i - count] = nums[i]
                nums.pop()

        pop_count = count
        while pop_count > 0:
            nums.pop()
            pop_count -= 1

        print(nums)
        print(count)

        return

if __name__ == '__main__':
    Solution().removeDuplicates(nums=[1,1,2])