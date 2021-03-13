"""
https://leetcode.com/problems/plus-one
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[len(digits) - 1] += 1
        n = 0
        while len(digits) - 1 - n != 0:

            if digits[len(digits) - 1 - n] == 10:
                # Carry over to next digit
                digits[len(digits) - 2 - n] += 1
                # Set current to zero
                digits[len(digits) - 1 - n] = 0
            n += 1  # Iterate to traverse

        # Edge case: [9 9 9 9] -> [1 0 0 0 0]
        if digits[0] == 10:
            digits[0] = 0

            # Shift everythign to the right once
            digits.append(digits[len(digits) - 1])
            for i in reversed(range(1, len(digits))):
                digits[i] = digits[i - 1]

            # Carry over
            digits[0] = 1
        return digits