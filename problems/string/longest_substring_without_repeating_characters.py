"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    """
    Sliding Window

    abcacde    distinct
    l r         {a,b,c}     add to set - a, b, c
    l  r        {a,b,c}     while s[r] in set, remove s[l]
    l r        {a,b,c}     remove a    then add s[r] = a
    l  r       {a,b,c}     while s[r] in set, remove s[l]
    lr       {a,c}       remove b,c  then add s[r] = c
    l  r     {a,c,d,e}   add to set - a, e

    Time O(n)
    Space O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = set()
        curr_length = 0
        max_length = 0
        left = 0
        for right in range(len(s)):     
            # Remove condition       
            while s[right] in distinct:
                    
                distinct.remove(s[left])
                left += 1
            
            # Add to set after removed
            distinct.add(s[right])
            
            # calculate total length
            curr_length = len(distinct)
            max_length = max(curr_length, max_length)
        
        return max_length