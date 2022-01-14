"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

:param s:
:return:
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # Sliding Window
        """
        Sliding Window

        Intuition: Check all the substring one by one to see if it has no duplicate character.

        For this problem, We use HashSet to store the characters in current window [i,j). Then we slide the index j to the
        right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point,
        we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i,
        we get our answer.

        Complexity:
        Time: O(2n) = O(n) in the worst case each character will be visited twice by ii and jj.
        Space: O(k) in which k is size of set or sliding window
        """
        left = max_length = 0
        repeats = set()

        # Use a set to determine if we got duplicates
        for right in range(len(s)):

            # When the right finds a duplicate, move the left pointer and constantly update set by removing left char.
            # The while loop will break once the repeated character is deleted by the left pointer
            while s[right] in repeats:
                repeats.remove(s[left])
                left += 1

            # Keep adding character to set to find repeats
            repeats.add(s[right])

            # Update max.
            max_length = max(max_length, right - left + 1)

        return max_length

    def lengthOfLongestSubstring_Eugene(self, s: str) -> int:  # Sliding Window
        """
        abcabcbb
        l r       abc   Traverse right pointer until all unique letters are added.
        l  r      abc   At this point, we right pointer is at a duplicate letter, so we enter the 'else' condition to start traversing the left pointer
         l r      bca   We traverse the left pointer until right pointer letter is removed from set
          l  r     cab
           l  r    abc
             l r   cb
               l   b        
        """
        max_length = 0
        duplicates = set()
        r = l = 0
        
        if s == "":
            return 0

        for r in range(len(s)): 
            # traverse right pointer until all unique letters are added
            if s[r] not in duplicates:
            
                # Add right pointer letters to set
                duplicates.add(s[r])
            
            # when right pointer letter already exists, we start traversing left pointer until that right pointer letter is removed from set
            else:                
                duplicates.remove(s[l])
                l += 1
                
            # Update max every iteration
            max_length = max(max_length, len(duplicates))

        return max_length

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abbcdeefghj"))

