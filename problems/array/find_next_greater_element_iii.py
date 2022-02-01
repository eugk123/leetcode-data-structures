"""
https://leetcode.com/problems/next-greater-element-iii/
"""
from typing import List
class Solution:
    """
    Linear Solution Constant Space

    21321   First pass, find the last ascending two numbers. save the left position.
     l

    21321   Second pass, find the minimum number that is greater than the left position.
     l r    We found that it's 2

    22311   When found, swap those two

    22311   From here, reverse everything after the left pointer.
     l
      311 -> 113
    result = 22113
    """
    def nextGreaterElement(self, n: int) -> int:
        
        def findSwapLeftIndex(digits):
            left = None
            
            # Find the last ascending adjacent numbers. Store the left pointer
            for i in range(1, len(digits)):
                if int(digits[i-1]) < int(digits[i]):
                    left = i - 1      
                    
            return left
                    
        def findSwapRightIndex(digits, left):
            right = None
            
            # From here, we find the right index by finding a number that's <= the left number and subtracting that index by 1
            for i in range(left + 1, len(digits)):
                if int(digits[i]) <= int(digits[left]):
                    right = i - 1
                    break

            # If we traversed all digits without setting the right index, we know we can swap the last digit
            if not right:
                right = i
            
            return right
        
        def swap(digits, left, right):
            tmp = digits[left]
            digits[left] = digits[right]
            digits[right] = tmp

        def reverse(digits, left, right):
            while left < right:
                swap(digits, left, right)
                left += 1
                right -= 1

        # Convert n to char array: digits
        digits_string = str(n)
        digits = []
        for digit in digits_string:
            digits.append(digit)
            
        # Edge case, len 1
        if n < 10:
            return -1
        
        # Find first swap left index
        left = findSwapLeftIndex(digits)

        # If no ascending adjacent numbers, we return -1
        if left is None:
            return -1
        
        # Find first swap right index
        right = findSwapRightIndex(digits, left)
        print(right)
        # Now swap the first two numbers
        swap(digits, left, right)
        
        # The remainder of the array from the left pointer should be descending
        # We simply need to reverse from left + 1 to make the entire digits the "next greater" number
        left = left + 1
        right = len(digits) - 1
        reverse(digits, left, right)
        
        result = int("".join(digits))
        if result > 2147483647:
            return -1
        
        
        return result