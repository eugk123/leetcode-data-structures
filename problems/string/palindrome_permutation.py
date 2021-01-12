"""
https://leetcode.com/problems/palindrome-permutation/
"""
class Solution:
    """
    Permutation of a string means another form of the string using the same characters and length.

    Ex: "abb" -> "bab"
    """
    def canPermutePalindrome(self, s: str) -> bool:
        # Check for odd number.
        remaining_singles = set()
        remainder = len(s) % 2

        # We'll use this set to keep track of how many single characters there are in the string.
        # If 0 chars & even len -> good.
        # If 1 char & odd len -> good
        for i in s:
            if i not in remaining_singles:
                remaining_singles.add(i)
            else:
                remaining_singles.remove(i)

        # For odd length, need to confirm all characters but one has duplicates
        if remainder == 1:
            if len(remaining_singles) == 1:
                return True
        # For even length, need to confirm all characters have duplicates
        if remainder == 0:
            if len(remaining_singles) == 0:
                return True

        return False



if __name__ == '__main__':
    print(Solution().canPermutePalindrome("ababab"))
