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