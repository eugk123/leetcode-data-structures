"""
https://leetcode.com/problems/longest-valid-parentheses
"""
class Solution:
    """
    Stack Linear Solution

    Example, with no additional close brackets
    ()(())) stack
    0123456 [-1]        initialize [-1] stack
    i       [-1,0]      open, add to stack
    i      [-1]        close, pop, if not empty, calculate length = index - peek = 0-(-1) = 2
    i     [-1,2]      open, add to stack
    i    [-1,2,3]    open, add to stack
        i   [-1,2]      close, pop, if not empty, calculate length = 4-2 = 2
        i  [-1]        close, pop, if not empty, calculate length = 5-(-1) = 6
        i []->[7]     close, pop, if empty, add current index

    Example, where close, pop, if empty requires adding in current index:
    ())()() stack
    0123456 [-1]        initialize [-1] stack
    i       [-1,0]      open, add to stack
    i      [-1]        close, pop, if not empty, calculate length = index - peek = 0-(-1) = 2
    i     []->[2]     close, pop, if empty, add current index
    i    [2,3]       open, add to stack
        i   [2]         close, pop, if not empty, calculate length = 4-2 = 2
        i  [2,4]       open, add to stack
        i [2]         close, pop, if not empty, calculate length = 8-4 = 4

    Time O(n)
    Space O(n)
    """
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        result = 0
        stack = [-1]
        for i in range(len(s)):
            letter = s[i]
                        
            if letter == "(":
                stack.append(i)
                
            elif letter == ")":
                
                left = stack.pop()

                if stack:
                    length = i - stack[len(stack) - 1]
                    result = max(length, result)
                if not stack:
                    stack.append(i)
        
        return result
              