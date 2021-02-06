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
        if len(nums) == 1 and target != nums[0]:
            return -1

        # Base Case: Check if target is on edges.
        left, right = 0, len(nums) - 1
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right

        # Check if array is sorted
        if nums[left] < nums[right]:
            # If we have a sorted array, we want to check if the edge values == target.
            if target < nums[left] or target > nums[right]:
                return -1
        else:
            # If it isn't sorted, then we first perform binary search to find the minimum value -- this is found due to
            # the inflection point. With the min index found, we can break this array into two sorted array and pick
            # the array that is within range of the target.
            while left < right:
                mid = int(left + (right - left) / 2)

                print(left, mid, right)
                # Closure - find min_index at inflection point
                if nums[mid] > nums[mid + 1]:
                    min_index = mid + 1
                    break
                elif nums[mid] < nums[mid - 1]:
                    min_index = mid
                    break

                # Traverse left/right pointer. Compare values between left and mid pointer.
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # With the minimum index, we can now figure out which sorted array to use.
            if target == nums[min_index]:
                return min_index
            elif target > nums[min_index] and target < nums[len(nums) - 1]:
                # Check between min_index and last index since that is always ascending -> Update left
                left = min_index
                right = len(nums) - 1
            else:
                # Else -> Update right
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
    nums = [6,7,0,1,2,4]
    target = 0
    print(Solution().search(nums, target))