"""
https://quastor.org/cracking-the-coding-interview/arrays-and-strings/check-permutation

The input is two strings. Check if the first string is a permutation of the second string.

Input - "wazup bro", " orbpuwaz"
Output - True
# the first character in " orbpuwaz" is a " "

Input - "hiiiya", "hiya"
Output - False
"""
def isPermutation(s1: str, s2: str) -> bool:
    """
    Hashmap Two Pass

    Make sure s1 and s2 have equal lengths.

    First pass - populate hash map (key: letter, val: count) with s1
    Second pass - check each letter of s2 and remove from hashmap if count == 1

    Finally, if hash map is empty, return True
    """
    if len(s1) != len(s2):
        return False

    letter_to_count = {}

    for letter in s1:
        if letter in letter_to_count:
            letter_to_count[letter] += 1
        else:
            letter_to_count[letter] = 1

    for letter in s2:
        if letter in letter_to_count:
            if letter_to_count[letter] == 1:
                letter_to_count.pop(letter)
            else:
                letter_to_count[letter] -= 1
        else:
            return False
    
    if len(letter_to_count) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = "wazup bro"
    s2 = " orbpuwaz"
    print("Same Length - True:", s1, s2, isPermutation(s1, s2))

    s1 = "hpya"
    s2 = "hiya"
    print("Same Length - False:", s1, s2, isPermutation(s1, s2))

    #Edge Case - different lengths
    s1 = "whale"
    s2 = "whplea"
    print("Different Lengths - False:", s1, s2, isPermutation(s1, s2))