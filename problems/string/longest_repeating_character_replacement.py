"""
https://leetcode.com/problems/longest-repeating-character-replacemente
https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Examples:
(1) Input:                  Output:
    s = "ABAB", k = 2       4
(2) Input:                  Output:
    s = "AABABBA", k = 1    4

Explanation
(1): Replace the two 'A's with two 'B's or vice versa.
(2): Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.

:param s:
:param k:
:return:
"""
def characterReplacement(s: str, k: int) -> int:  # Sliding Window
    """
    Intuition: Check all the substring one by one to see if it has no duplicate character.

    Algorithm: There's no edge case for this question. The initial step is to extend the window to its limit, that is,
    the longest we can get to with maximum number of modifications. Until then the variable start will remain at 0.

    Then as end increase, the whole substring from 0 to end will violate the rule, so we need to update start accordingly
    (slide the window). We move start to the right until the whole string satisfy the constraint again. Then each time we reach such situation, we update our max length.

    Complexity:
    Time:
    Space:
    """
    count = [0] * 26    # 26 zeroes because we want (key)ASCII integer to (val)Counts =
    start = maxCount = maxLength = 0

    for end in range(len(s)):
        # Grab the index for character count and update count
        index = ord(s[end]) - ord('A')  # ord() converts to ASCII value
        count[index] += 1

        # Update max count
        maxCount = max(maxCount, count[index])

        # While length is > k + maxCount, then traverse and remove count for start pointer
        while end - start + 1 > k + maxCount:
            index = ord(s[start]) - ord('A')
            count[index] -= 1
            start += 1

        # Update max length
        maxLength = max(maxLength, end - start + 1)
    return maxLength


if __name__ == '__main__':
    print(characterReplacement("ABACD", 2))