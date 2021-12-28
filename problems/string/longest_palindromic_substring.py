"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    """
    https://www.youtube.com/watch?v=y2BD4MJqV20
    """
    def longestPalindrome(self, s: str) -> str:
        """
        two pointer from center as you go left to right of the input
        Perform for both even and odd length palindromes
        Store all palindrome substrings in an array and also store max length
        
        Once you've reached the end, look for palindrome of max length and return that palindrome
        """
        # Two pointer expand from center when letters are not the same
        def checkPalindrome(left, right):
            if left >= 0 and right < len(s):            
                while s[left] == s[right]:
                    # Compute length to check if this substring is of max length
                    length = right - left + 1

                    # Update max indices and max length global variables
                    if length > self.max_length:
                        self.max_length = length
                        self.max_indices = (left, right)
                    left -= 1
                    right += 1
                    if left < 0 or right >= len(s):
                        break
                        
        if s == "":
            return ""
        
        self.max_indices = (0, 0)
        self.max_length = 0
        
        for i in range(len(s)):
            # odd palindromes
            checkPalindrome(i, i)
            
            # even palindromes
            checkPalindrome(i, i+1)
                                
        left, right = self.max_indices
        return s[left:right+1]


if __name__ == '__main__':
    print(Solution().longestPalindrome("abbabbadf"))
