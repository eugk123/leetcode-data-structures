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
    def lengthOfLongestSubstring_SlidingWindow(self, s: str) -> int:  # Sliding Window
        """
        Intuition: Check all the substring one by one to see if it has no duplicate character.

        Algorithm: A sliding window is an abstract concept commonly used in array/string problems. A window is a range
        of elements in the array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed,
        right-open). A sliding window is a window "slides" its two boundaries to the certain direction.

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

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring_SlidingWindow("abbcdeefghj"))

