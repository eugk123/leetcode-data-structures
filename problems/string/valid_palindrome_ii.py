"""
https://leetcode.com/problems/valid-palindrome-ii/
"""
class Solution:
    """
    Two Pass - Linear Time Constant Space
    Not the most optimal but still O(n) time and O(1) space.

    Trick is to try left only shifts on one pass and right only shifts on another pass.
    Count the number of shifts. There should only be at most 1 shift on one of those passes. If so, True. Otherwise, False.
    
    baaa
    l  r  shift left, then good
    abcbba
      lr  shift left, then good
    dffad
     l r  shift right, then good
    abcbbba
      l r shift right, then good

    Time O(n)
    Space O(1)
    """
    def validPalindrome(self, s: str) -> bool:
        # Shift in one direction when not equal. Do this both ways      
        left_shifts = 0
        right_shifts = 0
        
        # Try left
        left = 0
        right = len(s) - 1
        while left < right:            
            if left_shifts > 1:
                break
                
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                left += 1
                left_shifts += 1
                    
        # Try right
        left = 0
        right = len(s) - 1
        while left < right:
            if right_shifts > 1:
                break
                
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                right -= 1
                right_shifts += 1
                
        # print(right_shifts, left_shifts)
        if right_shifts > 1 and left_shifts > 1:
            return False
        return True
