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
        # The only base case is len of 1!
        if len(nums) == 1 and target == nums[0]:
            return 0
        if len(nums) == 1 and target != nums[0]:
            return -1

        min_index = 0

        # Binary search to find inflection point of min index
        left, right = 0, len(nums) - 1
        while left <= right:
            # Get middle index
            mid = int(left + (right - left) / 2)

            # Check if inflection point is found. You know that it is found when next number is > then previous.
            if mid > 0 and nums[mid - 1] > nums[mid]:
                min_index = mid
                break
            elif mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                min_index = mid + 1
                break

            # Traverse left and right pointers
            if nums[mid] > nums[left]:
                # Traverse left inwards because nums[mid] should be greater until inflection is found
                left = mid + 1
            else:
                right = mid - 1

        # Check where target lands on the array.
        # If it lands on the right of min_index, then update pointers from min_index -> end
        # Otherwise, update pointers from 0 to min_index - 1
        if target >= nums[min_index] and target <= nums[len(nums) - 1]:
            left, right = min_index, len(nums) - 1
        else:
            left, right = 0, min_index - 1

        # Typical binary search on sorted array looking for target
        while left <= right:
            # Get middle index
            mid = int(left + (right - left) / 2)

            # Check if target is found
            if nums[mid] == target:
                return mid

            # Traverse left and right pointers
            if nums[mid] < target:
                # Traverse left inwards because nums[mid] should be greater until inflection is found
                left = mid + 1
            else:
                right = mid - 1

        # If all else fails, then target doesn't exist in the array!
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [6,7,0,1,2,4]
    target = 0
    print(Solution().search(nums, target))