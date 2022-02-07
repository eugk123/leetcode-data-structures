"""
https://quastor.org/cracking-the-coding-interview/arrays-and-strings/one-away

You are given two strings as input. You want to find out if these two strings are at most one edit away from each other.

An edit is defined as either

inserting a character
removing a character
replacing a character

Input - "whale", "wrale"
Output - True

Input - "rake", "care"
Output - False

Input - "rake", "rake"
Output - True
"""
def isOneEditAway(s1: str, s2: str) -> bool:
    """
    Two Pointer. Iterate using shorter word to avoid index error.
    1) Left to right
    2) Right to left

    Count when letters are different

    If both counts are greater than 1, then return False
    Otherwise return True.

    If difference in length > 2, then return False

    ake     rake
    i->     i->     count=3
    <-i      <-i    count=0

    Time O(n)
    Space O(1)
    """
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) < len(s2):
        short = s1
    else:
        short = s2
    
    count = 0
    r_count = 0
    for i in range(len(short)):
        if s1[i] != s2[i]:
            count += 1
        if s1[len(s1) - i - 1] != s2[len(s2) - i - 1]:
            r_count += 1
    
    if count > 1 and r_count > 1:
        return False
    return True
def isOneEditAwayOld(s1: str, s2: str) -> bool:
    """
    Two Pointer starting at beginning of both inputs.

    Key here is considering the length of s1 and s2. When we run into different letters, we increment the index with the longer string, otherwise we increment together if strings are of equal length.       

    4 Cases:
    1. Insert/Remove
    whale
    whalpe

    2. Insert/Remove 2 or more
    whale
    whalppe

    3. Replace
    whale
    whape

    4. Replace 2 or more
    whale
    whapp
    """
    # Case 2 - Insert/Remove 2+ - If difference in length > 1, then return False
    if abs(len(s1) - len(s2)) > 1:
        return False

    # Check which string is of longer length, then set the longer and shorter strings
    if len(s1) > len(s2):
        longer = s1
        shorter = s2
    else:
        longer = s2
        shorter = s1
        
    count = 0
    j = 0
    for i in range(len(longer)):

        # when letters are different, add to count
        if longer[i] != shorter[j]:
            count += 1
            
            # longer length - traverse index
            if len(longer) > len(shorter):
                continue

            # same length - traverse both indices 
        j += 1
        
    if count > 1:
        return False

    return True                

if __name__ == '__main__':
    #Edge cases
    s1 = "a"
    s2 = "b"
    print("length 1 edge case - true", s1, s2, isOneEditAway(s1, s2))

    #True test cases
    s1 = "whale"
    s2 = "whalae"
    print("1. Insert/Remove", s1, s2, isOneEditAway(s1, s2))

    s1 = "whale"
    s2 = "whple"
    print("3. Replace", s1, s2, isOneEditAway(s1, s2))

    #Failure test cases
    s1 = "whale"
    s2 = "whalepp"
    print("2. Insert/Remove 2 or more", s1, s2, isOneEditAway(s1, s2))

    s1 = "whale"
    s2 = "waape"
    print("4. Replace 2 or more", s1, s2, isOneEditAway(s1, s2))

