"""
https://leetcode.com/problems/max-consecutive-ones-ii/
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Here you need to flip one zero and only return the maximum consective ones.

        # Edge case - len = 1
        if len(nums) == 1:
            return 1

        # So use a sliding window. Count the first zero, and get max count until you hit another zero.
        # Use a boolean to mark if the first zero is found.
        first_zero_found = False
        left = max_count = count = 0

        for right in range(len(nums)):
            # Duplicate zeroes, then have left pointer skip to right pointer.
            if right > 0 and nums[right] == 0 and nums[right - 1] == 0:
                left = right
                count = 1
                continue

            # First zero is found, mark boolean
            if nums[right] == 0 and not first_zero_found:
                first_zero_found = True

            elif nums[right] == 0 and first_zero_found:
                # If first index is zero, the while loop will never happen. Just move left pointer once.
                if left == right and nums[left] == 0:
                    left += 1
                    count -= 1

                else:
                    # Traverse left pointer until it passes the next 0
                    while nums[left] != 0:
                        left += 1
                        count -= 1

                    # Jump once more
                    left += 1
                    count -= 1

            count += 1
            max_count = max(count, max_count)

        return max_count
