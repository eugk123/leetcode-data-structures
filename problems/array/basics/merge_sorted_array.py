"""
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Base Case - all zero entries in nums1
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return

        # Start from right side of each array. Cal
        # Remember, n and m are length of populated entries in nums1 and nums2 respectively
        # Therefore, your curr pointer starts at n + m - 1!
        # Ex: [1,2,3,0,0,0] m = 3, [4,5,0] n = 2
        #     As you work backwards for this example, you want to start at index 3 + 2 - 1 = 4
        curr = n + m - 1
        i = m - 1
        j = n - 1

        while curr > -1:
            if j == -1:
                nums1[curr] = nums1[i]
                i -= 1
                curr -= 1
                continue

            if i == -1:
                nums1[curr] = nums2[j]
                j -= 1
                curr -= 1
                continue

            if nums1[i] >= nums2[j]:
                nums1[curr] = nums1[i]
                i -= 1
            else:
                nums1[curr] = nums2[j]
                j -= 1
            curr -= 1

if __name__ == '__main__':
    Solution().merge([-1,-1,0,0,0,0],4,[-1,0],2)