class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize result in case nothing is found
        res = [-1, -1]

        # If empty, return 0
        if not nums:
            return res

        # It fails when target is greater or less than the largest or smallest number respectively. So check the bounds real quick
        if target > nums[len(nums) - 1] or target < nums[0]:
            return res

        # Two part scan for far left and far right
        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right - left) // 2

            # Find target far left index - Check the beginning first
            if mid == 0 and nums[mid] == target:
                res[0] = mid
                break

            # Find target far left index via increase
            if nums[mid] == target and nums[mid] > nums[mid - 1]:
                res[0] = mid
                break

            # When they are equal, make sure the right pointer moves left.
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1

        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right - left) // 2

            # Find target far right index - Check the end first.
            if mid == len(nums) - 1 and nums[mid] == target:
                res[1] = mid
                break

            # Find target far right index via increase
            if nums[mid] == target and nums[mid] < nums[mid + 1]:
                res[1] = mid
                break

            # When they are equal, make sure the left pointer moves right.
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return res