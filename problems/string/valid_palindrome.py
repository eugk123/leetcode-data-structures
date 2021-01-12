"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def. palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Examples:
    Input:                              Output:
1)  "A man, a plan, a canal: Panama"    true
2)  "race a car"                        false

Constraints:
- s consists only of printable ASCII characters.
"""
def isPalindrome(s: str) -> bool:  # Two Pointer Solution
    """
    Intuition: One way to solve this problem is to create new string with only alphanumeric symbols and then check if
    it is palindrome. However we need O(n) space for this. There is more subtle approach, using Two Pointers technique.

    Algorithm:
        1. Start with beg = 0 and end = len(s) - 1, the first and the last symbols of string s.
        2. Now, we are going to move iterator beg only to the right and iterator end only to the left. Let us move them,
        until we reach alphanumeric symbols, using isalnum() function.
        3. Compare these two symbols. We are happy, if they are equal, or it is the same letter in different capitalization,
        for example q and Q. How to check this case? Make both symbols capitalized, using .upper() and compare them.
        4. In opposite case, immidietly return False.
        5. If we reached the end of or program and we did not return False, then we need to return True.

    Time: O(n), because we move beg only to the right and end only to the left, until they meet.
    Space: O(1), we just use a couple of additional variables.
    """
    # Two pointer solution
    # Convert to int and get value from both ends
    left = 0
    right = len(s) - 1

    while left <= right:
        # If the char is not a alpha character, traverse
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        # If left char == right char, traverse both
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome("abccb :A"))