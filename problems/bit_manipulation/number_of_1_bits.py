"""
https://leetcode.com/problems/number-of-1-bits
"""
class Solution:
    """
    https://www.youtube.com/watch?v=wLHhAHkID9M
    """
    def hammingWeight(self, n: int) -> int:
        """
        Bit Manipulation - O(1) Time with O(32) at every case

        For a 32-bit number, perform 32 iterations of the following:
        1. Use a mask = 1 (1-bit mask at far right),
        2. Calculate carry with given number n and mask. If carry > 0, add 1 to count.
        3. Left-shift mask once.  0001 -> 0010
        """
        # Iteration 0    Iteration 1    Iteration 2    Iteration 3
        # 1011 n         1011 n         1011 n         1011 n
        # 0001 mask      0010 mask      0100 mask      1000 mask
        # -------------  -------------  -------------  -------------
        # 0001 n & mask  0010 n & mask  0000 n & mask  1000 n & mask
        # count = 1      count = 2      count = 2      count = 3

        mask = 1
        count = 0
        for i in range(32):

            # If carry > 0, we +1 to count
            if n & mask > 0:
                count += 1

            # Shift 1-bit mask to the left to check if next bit is a 1.
            mask = mask << 1

        return count
