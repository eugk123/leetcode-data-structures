from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int(left + (right - left) / 2)
            print(left, mid, right)

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid


if __name__ == '__main__':
    print(Solution().findMin([2,3,1]))
