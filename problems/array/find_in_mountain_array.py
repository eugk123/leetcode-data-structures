"""
https://leetcode.com/problems/find-in-mountain-array
"""
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find peak index via binary search.
        left = 0
        right = mountain_arr.length() - 1
        while left <= right:
            mid = left + (right - left) // 2

            if mid > 0 and mountain_arr.get(mid - 1) < mountain_arr.get(mid) and mountain_arr.get(
                    mid) > mountain_arr.get(mid + 1):
                mid_index = mid
                break

            if mountain_arr.get(mid - 1) < mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid

        # Check if target is in ascending array. Make sure to check target is within bounds.
        left = 0
        right = mid_index
        print(left, right)
        if target >= mountain_arr.get(left) and target <= mountain_arr.get(right):
            while left <= right:
                mid = left + (right - left) // 2

                if mountain_arr.get(mid) == target:
                    return mid

                if mountain_arr.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid - 1

        # Check if target is in descending array. Make sure to check target is within bounds.
        left = mid_index
        right = mountain_arr.length() - 1
        if target <= mountain_arr.get(left) and target >= mountain_arr.get(right):
            while left <= right:
                mid = left + (right - left) // 2
                print(mid)

                if mountain_arr.get(mid) == target:
                    return mid

                if mountain_arr.get(mid) > target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
