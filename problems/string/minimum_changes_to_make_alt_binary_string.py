"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
"""
class Solution:
    def minOperations(self, s: str) -> int:
        # Base case, size of 1
        if len(s) == 1:
            return 0

        # Force 10101010....
        res1 = 0
        for i in range(len(s)):
            # If index is even, val should be 1
            # If index is odd, val should be 0
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                continue
            else:
                res1 += 1

        # Force 010101010....
        res0 = 0
        for i in range(len(s)):
            print(s[i])
            # If index is even, val should be 0
            # If index is odd, val should be 1
            if (i % 2 == 0 and s[i] == '0') or (i % 2 == 1 and s[i] == '1'):
                continue
            else:
                res0 += 1

        return min(res1, res0)