"""
https://leetcode.com/problems/next-permutation/submissions/
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Two Pointer Three Pass - Linear Time Constant Space
        Same as https://leetcode.com/problems/next-greater-element-iii/

        21345 -> 21354  last two swap
        21354 -> 21435  swap 3 and 4, then reverse the after 4
        21435 -> 21453  last two swap
        435971 -> 437159   swap 5 and 7, then reverse after 7

        First pass - find last two ascending numbers using i and i-1 then assign left = i-1.
        435971
           i    left = i-1 = 2
        
        Second pass - from the left pointer to the end of nums, find the next greater number and assign right = i
        435971
          l r   right = i, 7 is the next greater number. NOT 9.
        
        Swap the two numbers, then reverse after left index (left + 1).
        437951  numbers swapped
        437159  after left pointer, the rest is reversed
        """
        def reverse(nums, left=0):
            # reverse numbers after left index
            right = len(nums) - 1
            while left < right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
        
        # no permutation if len == 1
        if len(nums) == 1:
            return nums
        
        left = None
        right = None
        
        # first pass
        # look for last ascending number and assign left pointer left of it
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                left = i-1
        
        # if no left pointer assigned, it means we need to reverse the whole thing
        if left == None:
            reverse(nums)
            return nums
        
        # second pass
        # after assigning left pointer, look for the nearest greater number and assign right pointer to that number
        # there will always be a right pointer because if left pointer is assigned, it at least means the next number is greater
        next_minimal_greater_number = math.inf
        for i in range(left, len(nums)):
            if nums[i] > nums[left]:
                next_minimal_greater_number = min(nums[i], next_minimal_greater_number)
                right = i
        
        # swap the left and right pointers
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        
        # then reverse after left pointer
        reverse(nums, left + 1)
        return nums
        