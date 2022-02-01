"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
from typing import List
class Solution:
    """
    Stack

    Try out each example and figure out the conditions. See my scratch board below.    
    I noticed that each operator, you'll pop twice from stack then compute, then add back to stack.

    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    10 6 9 3
    + -> 3 + 9 = 12
    10 6 12 -11
    * -> -11 * 12 = -132
    10 6 -132
    / -> 6 / -132 = 0
    10 0
    * -> 0 * 10 = 0
    0 17
    + -> 0 + 17 = 17
    17
    + -> 0 + 5 = 5

    ["3","11","5","+","-"]
    3 11 5
    + -> 5 + 11 = 16
    3 16
    - -> 3 - 16
    -13
    """
    def evalRPN(self, tokens: List[str]) -> int:
        # RPN is combining last two using the operator. So if +, add them together.
        stack = []
        for token in tokens:

            # We need to traverse until we reach the operator and take the last two. This can be done using a stack and popping the last two values then adding it back into the stack.
            if token == "+" or token == "-" or token == "*" or token == "/":

                # We asssume problem will always be a valid RPN, so we do not need to worry about returning if stack is empty.
                first = stack.pop()
                second = stack.pop()
            else:
                # Need to continuously cast to int if not one of the operators.
                stack.append(int(token))

            # Need a bunch of if conditions to tell us whether we add, subtract, divide, or multiply based on the element operator string.
            if token == "+":
                stack.append(second + first)

            if token == "-":
                stack.append(second - first)

            if token == "*":
                stack.append(second * first)

            if token == "/":
                # Problem asks to floor when divided. so cast again.
                stack.append(int(second / first))

        return stack.pop()

    def evalRPNEugene(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        if len(tokens) == 1:
            return tokens[0]
        
        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                curr = int(stack.pop())
                
                if token == "+":
                    total = int(stack.pop()) + curr
                if token == "-":
                    total = int(stack.pop()) - curr
                if token == "*":
                    total = int(stack.pop()) * curr
                if token == "/":
                    total = int(int(stack.pop()) / curr)
                stack.append(total)
            else:
                stack.append(token)
        return stack[0]