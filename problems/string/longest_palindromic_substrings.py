"""
https://leetcode.com/problems/palindromic-substrings/
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        https://www.youtube.com/watch?v=4RACzI5-du8
        
        At every index, we expand from center to check for valid palindromes.
        
        When we expand, we need to expand twice with center size 1 for odd-sized palindromes and center size 2 for even-sized palindromes 
        
        While n = len(s)...
        Time Complexity: O(n^2)
        Having to iterate through an array then iterate again at every index results in n^2 time complexity.

        Space Complexity: O(1)
        We are not introducing additional memory. We are simply using the input and iterating through it. We are only adding constants.
        """
        result = 0
        
        for i in range(len(s)):
            # Palindrome center size of 1 for odd-size substrings
            left = i
            right = i
            if left >= 0 and right < len(s):
                while s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1

                    if left < 0 or right >= len(s):
                        break

            # Palindrome center size of 2 for even-size substrings
            left = i
            right = i + 1
            if left >= 0 and right < len(s):
                while s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1

                    if left < 0 or right >= len(s):
                        break

        return result
        