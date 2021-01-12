from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=jzZsG8n2R9A
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array - O(nlogn) time
        nums.sort()

        res = []

        # Iterate current pointer as the target and Use L and R pointer (binary search) for each iteration
        for curr in range(len(nums)):

            # Since curr is one step behind left, if they are equal, traverse both to the right 1 step
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            # Update pointers
            left = curr + 1
            right = len(nums) - 1

            # Search between left and right pointer for any 3sum combinations
            while left < right:
                three_sum = nums[left] + nums[right] + nums[curr]

                # Found combination when L + R = C
                if three_sum == 0:
                    res.append([nums[left], nums[right], nums[curr]])
                    left += 1
                    # left pointer duplicate traversal
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                # If sum < 0 -> move left pointer
                if three_sum < 0:
                    left += 1

                # If sum > 0 -> move right pointer (this also takes care of right pointer duplicates)
                if three_sum > 0:
                    right -= 1

        return res

if __name__ == '__main__':
    print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))
