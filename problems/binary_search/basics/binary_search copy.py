"""
https://leetcode.com/problems/binary-search/
"""
from typing import List
class Solution:
    def binary_search(self, nums, target):

        
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] == target:
                return left
            if nums[mid] == target:
                return mid
            if nums[right] == target:
                return right
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
"""
1 2 3 4 5 6 7 8 9 10
l       m          r
l       
"""
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,21,90,100,101,102,103,106,108,209,301,306,400]
    target = 21

    target_index = Solution().binary_search(nums, target)
    print(target, nums[target_index])
