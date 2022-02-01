"""
https://leetcode.com/problems/next-greater-element-i/
"""
class Solution:
    """
    For linear time O(n), this is not an easy problem. The trick is you need to create a map that tells the 'next greater number' for every number in nums2.
    
    Therefore, iterate through nums2 first, create that map. You're gonna need a stack for this.
    
    Then finally iterate through nums1 and use that next_greater_number map to populate the result.
    
    max value = 5
    5 3 1 4 2   stack   map 
    i           [5]     {}  curr <= stack.peek(), add to stack
      i         [5 3]   {}  curr > stack.peek(), stack.pop(), and add to map via next_greater_number[stack.pop()] = curr
        i       [5 3 1] {}  curr > stack.peek(), stack.pop(), and add to map
          i     [5 3]   {}  [continuously] curr <= stack.peek(), add to stack
          i     [5]     {}  [continuously] curr <= stack.peek(), add to stack
          i     [5 4]   {}  curr > stack.peek(), add to stack
            i   [5 4 2] {}  curr <= stack.peek(), add to stack
    
    at the end, we need to set the remaining values in stack to map as -1
    This results in:    {5:-1, 3:4, 1:4, 4:-1, 2:-1}
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # First pass - populate next_greater_number map via nums2
        stack = []
        next_greater_number = {}
        for num in nums2:
            # If stack is empty, or if num is less than or equal to peek, we just append.
            # Otherwise, if num is greater than peak, we pop and set previous number to greater number
            if stack:
                while num > stack[len(stack) - 1]:
                    next_greater_number[stack.pop()] = num
                    
                    if not stack:
                        break
            stack.append(num)
                
        # Rest of values in stack are numbers without a greater next number
        while stack:
            next_greater_number[stack.pop()] = -1

        # Second pass - get result using map
        result = []
        for num in nums1:
            result.append(next_greater_number[num])
            
        return result
            