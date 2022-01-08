"""
https://leetcode.com/problems/palindrome-permutation/

Permutation of a string means another form of the string using the same characters and length.

Ex: "abb" -> "bab"
"""
def canPermutePalindrome(s: str) -> bool:
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

def canPermutePalindromeEugene(s: str) -> bool:
    """
    Hash Two Pass

    Successful examples with letter counts:
    aba         a: 2, b: 1
    aabb        a: 2, b: 2
    abbba       a: 2, b: 3
    aabbaa      a: 4, b: 2
    baaacaaab   a: 6, b: 2, c: 1
    abcba       a: 2, b: 2, c: 1

    So as long as we have only 0 or 1 odd count of a single letter and the rest are even count, we are good

    Edge Cases
    a       1 letter result
    aa      2 same letter result 

    Time Complexity: O(n) with two pass
    Space Complexity: O(n) with additional hashmap
    """
    if len(s) == 1:
        return True
    
    if len(s) == 2:
        if len(set(s)) == 1:
            return True
    
    # First pass, count all letters
    letter_to_count = {}
    for letter in s:
        if letter not in letter_to_count:
            letter_to_count[letter] = 1
        else:
            letter_to_count[letter] += 1
    
    even_count = 0
    odd_count = 0
    # Second pass, count number of evens and number of odds
    for letter in letter_to_count:
        
        # Odd Even checks can work by simple math. Integer will always floor the number.
        # Odd results in both being equal
        # 1/2 = 0   (1-1)/2 = 0 
        # 3/2 = 1   (3-1)/2 = 1 
        # Even results in not equal
        # 2/2 = 1   (2-1)/2 = 0
        # 4/2 = 2   (4-1)/2 = 1
        if int(letter_to_count[letter]/2) == int((letter_to_count[letter]-1)/2):
            odd_count += 1
        else:
            even_count += 1

    if odd_count > 1:
        return False

    return True


if __name__ == '__main__':
    s = "a"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))
    
    s = "aa"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))

    s = "aab"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))

    s = "code"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))

    s = "carerac"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))

    s = "aassdddeff"
    print("s={}, result={}".format(s, canPermutePalindromeEugene(s)))
