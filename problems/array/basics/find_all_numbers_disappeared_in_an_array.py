"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
from typing import List
class Solution:
    """
    O(n) time w/ O(n) space -> simply use HashMap or HashSet.

    But a more optimal solution maintaining time and having O(1) space, take advantage of the constraints.

    Given a range 1, n (size of array) and all elements are positive. What you can do is mark the element with a negative
    number if it is contained. 2nd pass, if not negative, then we know that is missing!
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        # Example:
        # [1,2,4,4,5]
        # The values are in between 1 < nums[i] < len(nums) = 5
        # Therefore, we can utilize the value of the indices! We mark the indices as negative so our second pass
        # can identify them
        # 1-1, 2-1, 4-1, PASS, 5-1 -> Mark 0, 1, 3, and 4 as negative -> [-1,-2,4,-4,-5]

        for i in range(len(nums)):
            # Set the current value as an index (need to -1). Then mark it by making it negative.
            mark_index = abs(nums[i]) - 1

            # Since we have duplicates, we don't want to mark again; if we do, it'll turn positive.
            if nums[mark_index] > 0:
                nums[mark_index] = nums[mark_index] * -1

        # On second pass we check if any values are positive and add those indices as the result.
        for i in range(1, len(nums) + 1):
            # Remember, in an array, we'll have to subtract 1 since index starts at 0.
            if nums[i - 1] > 0:
                res.append(i)

        return res