"""
https://leetcode.com/problems/single-number
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        Bit Manipulation is the only way to achieve O(n) time with O(1) space

        You can use hash map for O(n) time, but will ad O(n) space.

        Welcome exclusive-or XOR (^)!
        1. XOR of a and 0 returns a: a^0 = a
        2. XOR of a and a returns 0: a^a = 0

        Therefore, since we have all duplicates except for 1, we can simply perform
        something like this: a^b^a = (a^a)^b = b

        So (a^a^..^n^n)^b = 0^b = b
        """
        a = 0
        for i in nums:
            a ^= i
        return a

