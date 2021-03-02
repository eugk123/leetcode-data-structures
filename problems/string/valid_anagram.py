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
    # If different lengths, return False
    if len(s) != len(t):
        return False

    # Initialize map to check for anagrams
    map = {}

    # Populate first input
    for letter in s:
        # Add new letter to map
        if not map.get(letter):
            map[letter] = 1

        # If duplicate, add 1 to count
        else:
            map[letter] += 1

    # Check map against second input
    for letter in t:
        # If letter not in map, return False
        if not map.get(letter):
            return False

        # If it is in map, subtract 1
        elif map.get(letter):
            map[letter] -= 1

        # If count == 0, then pop that letter
        if map.get(letter) == 0:
            map.pop(letter)

    # If not returned False, we know s & t are anagrams of each other.
    return True

if __name__ == '__main__':
    print(isAnagram("abcaaa", "aacaba"))
