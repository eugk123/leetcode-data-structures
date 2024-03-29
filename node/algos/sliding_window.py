from typing import List
import math
"""
Algorithm: A sliding window is an abstract concept commonly used in array/string problems. A window is a range
of elements in the array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed,
right-open). A sliding window is a window "slides" its two boundaries to the certain direction.

Time Complexity of this algorithm should result in linear time O(n)
"""
# Length of longest substring without repeating characters
def sliding_window(s: str) -> int:  # Sliding window                                                                          
    result = 0
    unique_letters = set()

    # Use a set to determine if we got duplicates
    left = 0
    for right in range(len(s)):

        # When condition is met (right finds duplicate),
        # Continuously move left pointer and remove from set.
        # The while loop will break once the repeated character is removed.
        while s[right] in unique_letters:
            unique_letters.remove(s[left])
            left += 1

        # Keep adding character to set to find repeats
        unique_letters.add(s[right])

        # Update max.
        result = max(result, right - left + 1)

    return result

def sliding_window_array(nums:List[int]):

    current_sum = 0
    max_sum = -math.inf
    l = 0
    
    # Sliding window problems will end once r passes the final index.
    for r in range(len(nums)):
        current_sum += nums[r]
        max_sum = max(current_sum, max_sum)
        

        # Slide left pointer (could be single move such as an if condition or iterative move using while loop)       
        if current_sum <= 0:
            l = r + 1
            current_sum = 0
        
        # Slide right pointer
        r += 1
        
    return max_sum


def sliding_window_string(s:str):

    letter_frequency = {}  # letter frequency map
    l = 0   # initialize left pointer
    max_length = 0  # initialize max or min length to lowest or highest possible value respectively.

    # count the frequencies for chars in 
    for letter in s:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    # Sliding window problems will end once r passes the final index.
    for r in range(len(nums)):
        current_sum += nums[r]
        max_sum = max(current_sum, max_sum)
        

        # Slide left pointer (could be single move such as an if condition or iterative move using while loop)       
        if current_sum <= 0:
            l = r + 1
            current_sum = 0
        
        # Slide right pointer
        r += 1
        
    return max_sum