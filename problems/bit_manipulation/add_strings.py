"""
https://leetcode.com/problems/add-strings
"""
class Solution:
    """
    Simple bit-by-bit addition using a carry.
    """
    def addStrings(self, num1: str, num2: str) -> str:

        # Edge cases
        if not num2:
            return num1
        if not num1:
            return num2
        if not num1 and num2:
            return num1

        # We want num1 to be longer than num2, so swap if it's less.
        # This allows us to traverse through the longer string.
        if len(num1) < len(num2):
            temp = num1
            num1 = num2
            num2 = temp

        carry = 0
        j = len(num2) - 1
        res = deque([])
        for i in reversed(range(len(num1))):

            # For every iteration, we check the carry.
            if j >= 0:
                current_sum = int(num1[i]) + int(num2[j]) + carry
                if current_sum > 9:
                    res.appendleft(str(current_sum)[1])
                    carry = 1
                else:
                    res.appendleft(str(current_sum)[0])
                    carry = 0
                j -= 1
            else:
                current_sum = int(num1[i]) + carry
                if current_sum > 9:
                    res.appendleft(str(current_sum)[1])
                    carry = 1
                else:
                    res.appendleft(str(current_sum)[0])
                    carry = 0

        if carry == 1:
            res.appendleft("1")

        return "".join(res)