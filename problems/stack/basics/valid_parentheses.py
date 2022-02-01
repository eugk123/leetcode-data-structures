"""
https://leetcode.com/problems/valid-parentheses
"""
class Solution:
    def isValid(self, s: str) -> bool:

        # ex: s = '()[]{}'
        # '('         [')']
        # '()'        []          .pop() = ')'
        # '()['       [']']
        # '()[{'      [']','}']
        # '()[{}'     [']']       .pop() = '}'
        # '()[{}]'    []          .pop() = ']'

        stack = []
        map = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            # If char is a open bracket, add the close bracket to stack
            if char in map:
                stack.append(map.get(char))

            # If char is a close bracket
            elif char not in map:

                # If stack empty, False
                if not stack:
                    return False

                # If stack not empty, close bracket is not the last element of stack.
                elif char != stack.pop():
                    return False

        # Stack should be empty after traversing through entire string.
        if stack:
            return False

        return True


    def isValidEugene(self, s: str) -> bool:
        
        # Populate map open to close paren
        open_to_close = {}
        open_to_close["{"] = "}"
        open_to_close["["] = "]"
        open_to_close["("] = ")"
        
        stack = []

        for letter in s:
            # If close parentheses, we check stack to compare
            if letter not in open_to_close:
                # If we got no stack, then return false
                if not stack:
                    return False
            
                # If the closing paranthesis matches top of stack, then continue; otherwise, return false
                if letter == stack.pop():
                    continue
                else:
                    return False

            # If open parentheses, we get the close parentheses from map then add to stack to track order.
            else:
                stack.append(open_to_close[letter])
        
        # If stack still has elements, it means there are more open than close. So return false.
        if stack:
            return False
        
        return True