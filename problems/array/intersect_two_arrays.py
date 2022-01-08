"""
https://leetcode.com/problems/intersection-of-two-arrays/

Intersection of two arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

ex1:
nums1=[1,2,2,1]
nums2=[2,2]
output=[2]

ex2:
nums1=[4,9,5]
nums2=[9,4,9,8,4]
output=[9,4]   or   [4,9]
"""
from typing import List
class Solution:
    """
    Two Pass Hashmap Solution.

    Time Complexity: O(n) with two linear loops
    Space Complexity: O(n) with the creation of additional collections of n length

    Question -- do we want to perform O(1) space?
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # input: nums1=[1,2,2,1], nums2=[2.2]
        # first pass, create two hashsets: set1 = {1,2}, set2 = {2}
        # set1 will be longer length than set2
        set1 = set()
        set2 = set()
        result = []

        if len(nums1) > len(nums2):
            for i in range(len(nums1)):
                set1.add(nums1[i])
                if i < len(nums2):
                    set2.add(nums2[i])

        else:
            for i in range(len(nums2)):
                set1.add(nums2[i])
                if i < len(nums1):
                    set2.add(nums1[i])

        # second pass, check if each element in set2 is in set1, and if exists, add to result.
        # set2 is of less length and as we check for each number in set2 in set1, this is the most optimal time complexity since lookups in sets are O(1) time.
        for num in set2:
            if num in set1:
                result.append(num)
        
        return result

if __name__ == '__main__':
    nums1, nums2 = [1,2,2,1], [2,2]
    print("nums1={}, nums2={}, result={}".format(nums1, nums2, Solution().findIntersectedElements(nums1, nums2)))

    nums1, nums2 = [4,9,5], [9,4,9,8,4]
    print("nums1={}, nums2={}, result={}".format(nums1, nums2, Solution().findIntersectedElements(nums1, nums2)))

    nums1, nums2 = [1], [2]
    print("nums1={}, nums2={}, result={}".format(nums1, nums2, Solution().findIntersectedElements(nums1, nums2)))
