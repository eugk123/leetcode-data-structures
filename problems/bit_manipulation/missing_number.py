"""
https://leetcode.com/problems/missing-number
"""
from typing import List
class Solution:
    """
    Bit Manipulation -> O(N) Time, O(1) Space

    Other options:
    Brute Force -> N^2 Time w/ Constant Space
    Sorting -> NlogN Time w/ Constant Space
    HashSet/Queue 2-pass -> N Time w/ N Space
    """
    def missingNumber(self, nums: List[int]) -> int:
        # Same as single number, recognize that the indices and the range of numbers will provide a pair of duplicates except for the missing number.
        # Example below, with the given nums array, you need to consider the final index to be able to find the missing number via xor operations.
        # Remember the properties of xor: (1) a^0 = a and (2) a^a = 0 -> finally, (3) a^b^a = b
        # [0 1 2 3 4] -> [0 1 2 4]
        #  0 1 2 3 4      0 1 2 3 (4)
        missing_number = len(nums)  # 4
        for i in range(len(nums)):
            # 4^0^0 -> 4^0^0^1^1 -> 4^0^0^1^1^2^2 -> 4^0^0^1^1^2^2^3^4 = 3
            missing_number = missing_number ^ i ^ nums[i]

        return missing_number