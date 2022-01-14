"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Sliding Window w/ Set

Use hashset to count total distinct characters.

If len(set) <= k, add to set using right, calculate length, move right pointer.
If len(set) > k, remove from set using left, move left pointer (edge case: repeat letters, use while loop)

eceba  k=2 -> 
r       {e1} len(map) <= k, res = 1
lr      {e1 c1} len <= k, res = 2
l r     {e2 c1} len <= k, res = 3
l  r    {e2 c1 b1} len > k, need to remove using left pointer
 l r    {e1 c1 b1}
  lr    {e1 b1} len <= k, res = 2
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        def addToMap(letter, hash_map):
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
                
        def removeFromMap(letter, hash_map):
            if letter in hash_map:
                hash_map[letter] -= 1
                if hash_map[letter] == 0:
                    hash_map.pop(letter)
                    
        letter_frequency = {}
        max_length = 0
        left = 0

        for right in range(len(s)):

            # Add every new letter to map via right pointer.
            addToMap(s[right], letter_frequency)
            
            # If at most K distinct characters, move right pointer & calculate max            
            if len(letter_frequency) <= k:
                max_length = max(right - left + 1, max_length)
                continue

            # If more than K distinct characters, move left pointer, and remove from set
            while len(letter_frequency) > k:
                # Keep going if left pointer repeats previous letter  
                removeFromMap(s[left], letter_frequency)
                left += 1

        return max_length