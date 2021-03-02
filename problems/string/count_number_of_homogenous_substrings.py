"""
https://leetcode.com/problems/count-number-of-homogenous-substrings/
"""
class Solution:
    def countHomogenous(self, s: str) -> int:
        # For every duplicate letter found, we add the current len() to prev len()
        # a = 1 = len(a)
        # aa = 1 + 2 = len(a) + len(aa)
        # aaa = 1 + 2 + 3 = len(a) + len(aa) + len(aaa)

        total = 0
        duplicates = []
        for i in range(len(s)):
            # If next letter is different from previous, restart duplicates
            if i > 0 and s[i - 1] != s[i]:
                duplicates = []

            # Append
            duplicates.append(s[i])

            # For first letter, add 1 to total
            if len(duplicates) == 1:
                total = total + 1

            # For subsequent duplicates, add the total length
            elif i > 0 and s[i - 1] == s[i]:
                total = total + len(duplicates)

        return total % (10 ** 9 + 7)