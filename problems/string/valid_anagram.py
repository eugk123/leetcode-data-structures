"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Follow-up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
def isAnagram(s: str, t: str) -> bool:  # HashMap
    """
    Inituition: Use HashTable. Add to table first. Then check.

    Complexity:
    Time: O(2n) = O(n)
    Space: O(1) = Although we do use extra space, the space complexity is O(1) because the table's size stays constant
    no matter how large n is.

    """
    if len(t) != len(s):
        return False

    char_map = dict()
    for i in range(len(s)):
        if s[i] in char_map:
            char_map[s[i]] += 1  # Add duplicate counter +1
        else:
            char_map[s[i]] = 2  # Start at 2 instead of 1.
    print(char_map)

    for i in range(len(t)):
        print(i)
        if t[i] in char_map and char_map[t[i]] > 0:  # Checks to see if t char exists in map and the number of duplicates are expected
            char_map[t[i]] -= 1  # Remove duplicate counter -1
        if t[i] not in char_map:
            return False
        if t[i] in char_map and char_map[t[i]] == 0:  # When value is at 0, this means t has more duplicate characters than s
            return False
    print(char_map)  # Should result in {'a': 1, 'b': 1, 'c': 1} for
    return True

if __name__ == '__main__':
    print(isAnagram("abcaaa", "aacaba"))
