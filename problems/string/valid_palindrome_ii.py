"""
https://leetcode.com/problems/valid-palindrome-ii/
"""
class Solution:
    """
    My solution does multiple passes by using the isPalindrome method.

    Not the most optimal but still O(n) time and O(1) space.
    """
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            left = 0
            right = len(s) - 1

            while left <= right:
                # If the char is not a alpha character, traverse
                if not s[left].isalnum():
                    left += 1
                    continue
                if not s[right].isalnum():
                    right -= 1
                    continue

                # If left char == right char, traverse both
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        # Start at both ends. Work inwards.
        left, right = 0, len(s) - 1

        skip_count = 0
        while left < right:

            # If equal, traverse inwards
            if s[left] == s[right]:
                left += 1
                right -= 1

            # If not equal
            else:
                # Try both
                # (1) deleting left index then check if palindrome
                # (2) deleting right index then check if palindrome
                if not isPalindrome(s[0:left] + s[left + 1:]) and not isPalindrome(s[0:right] + s[right + 1:]):
                    return False
                else:
                    return True
        return True
