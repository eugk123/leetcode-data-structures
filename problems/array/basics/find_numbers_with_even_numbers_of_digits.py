"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        # Take the length of the digits to determine odd or even
        for num in nums:
            # To determien odd or even, check remainder via modulus
            # remainder = 1 -> Odd
            # remainder = 0 -> Even
            remainder = len(str(num)) % 2
            if remainder == 1:
                continue
            elif remainder == 0:
                count += 1
        return count