"""
https://leetcode.com/problems/add-binary
"""
from collections import deque
class Solution:
    """
    Simple bit-by-bit addition using a carry.
    """
    def addBinary(self, a: str, b: str) -> str:
        # Edge cases
        if not b:
            return a
        if not a:
            return b
        if not a and b:
            return a

        # We want a to be longer than b, so swap if it's less.
        # This allows us to traverse through the longer string.
        if len(a) < len(b):
            temp = a
            a = b
            b = temp

        carry = 0
        j = len(b) - 1
        res = deque([])
        for i in reversed(range(len(a))):

            # For every iteration, we check the carry.
            if j >= 0:
                current_sum = int(a[i]) + int(b[j]) + carry
                if current_sum == 3:
                    res.appendleft("1")
                    carry = 1
                elif current_sum == 2:
                    res.appendleft("0")
                    carry = 1
                elif current_sum == 1:
                    res.appendleft("1")
                    carry = 0
                else:
                    res.appendleft("0")
                    carry = 0
                j -= 1
            else:
                current_sum = int(a[i]) + carry
                if current_sum == 2:
                    res.appendleft("0")
                    carry = 1
                elif current_sum == 1:
                    res.appendleft("1")
                    carry = 0
                else:
                    res.appendleft("0")
                    carry = 0

        if carry == 1:
            res.appendleft("1")

        return "".join(res)
