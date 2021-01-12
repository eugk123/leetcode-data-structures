"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
NOTE: One of the test cases contain a non-sorted array. Don't know how to pass this. ex: nums = [1,3] target = 3 -> 1
"""
from typing import List
class Solution:
    """
    Binary Search Algorithm - 2 Pass for Rotated Array
    Note: nums is guaranteed to be rotated at some pivot.

    1. Rotated Array -> Find min index
    2. Set indices for a Sorted Array
    3. Sorted Array -> Find target
    """
    def search(self, nums: List[int], target: int) -> int:
        # Base Case: len(nums) = 1
        if len(nums) == 1 and target == nums[0]:
            return 0
        elif len(nums) == 1 and target != nums[0]:
            return -1

        # First perform binary search to convert rotated array to a sorted array.
        # To do so, first find the min number index
        left = min_index = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            print(nums[mid], mid)
            # Closure - find min_index at inflection point
            if nums[mid] > nums[mid + 1]:
                min_index = mid + 1
                break
            elif nums[mid] < nums[mid - 1]:
                min_index = mid
                break

            # To traverse left/right pointer
            if nums[left] < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        print(min_index)
        # With min number, compare the target with the min number to determine whether to update left or right pointer
        if target == nums[min_index]:
            return min_index
        # Check between min_index and last index since that is always ascending -> Update left
        elif target > nums[min_index] and target < nums[len(nums) - 1]:
            left = min_index
            right = len(nums) - 1
        # Else -> Update right
        else:
            right = min_index
            left = 0

        # Perform binary search again to find target using the sorted array.
        while left <= right:
            mid = int(left + (right - left) / 2)

            # Closure Case: target == num[mid]
            if target == nums[mid]:
                return mid

            # Traverse right or left pointer based on these conditions:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [4, 5, 6, 7]
    target = 5
    # nums = [5,6,0,1,2,3,4]
    # target = 11
    print(Solution().search(nums, target))