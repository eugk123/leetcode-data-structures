"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    """
    https://www.youtube.com/watch?v=y2BD4MJqV20
    """
    def longestPalindrome(self, s: str) -> str:
        # Base Case: len = 1
        if len(s) == 1:
            return s

        max_length = 0  # To grab longest palindrome
        store_right = [0]
        store_left = [0]

        # Iterate through string
        for i in range(len(s)):
            # We are starting from 2nd index -> i > 0
            if i > 0:
                # Case 1: duplicate centers
                right, left = i, i - 1
                while s[right] == s[left]:
                    if right - left > max_length:
                        store_right[0] = right
                        store_left[0] = left
                        max_length = right - left
                    right += 1
                    left -= 1
                    if left < 0 or right > len(s) - 1:  # This breaks the while loop when indices go out of bounds
                        break

                # Case 2: unique center
                right, left = i, i
                while s[right] == s[left]:
                    if right - left > max_length:
                        store_right[0] = right
                        store_left[0] = left
                        max_length = right - left
                    right += 1
                    left -= 1
                    if left < 0 or right > len(s) - 1:
                        break

        res = ''
        for i in range(store_left[0], store_right[0] + 1):
            res += s[i]

        return res

        # Upon completion, get palindrome using the stored right and left indices


if __name__ == '__main__':
    print(Solution().longestPalindrome("abbabbadf"))
