"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""
class Solution:
    def modifyString(self, s: str) -> str:

        def modifyString(self, s: str) -> str:
            res = ''

            # Base Case
            if len(s) == 1 and s == '?':
                return 'a'
            elif len(s) == 1:
                return s[0]

            for i in range(len(s)):
                if s[i] == '?':

                    # Try a, b, or c
                    for char in ['a', 'b', 'c']:

                        # First index - Avoid repeating right index char (don't worry about out of bound
                        # index since we confirmed base case of len = 1 above)
                        if i == 0 and s[i + 1] != char:
                            res += char
                            break

                        # Last index - Avoid repeating left index char (this will be from result.)
                        if i == len(s) - 1 and res[i - 1] != char:
                            res += char
                            break

                        # Both sides occupied - Avoid repeating left index char (this will be from result)
                        # and right index char
                        if i > 0 and res[i - 1] != char and s[i + 1] != char:
                            res += char
                            break
                else:
                    res += s[i]
            return res

if __name__ == '__main__':
    print(Solution().modifyString(s='abc?abc?abc'))