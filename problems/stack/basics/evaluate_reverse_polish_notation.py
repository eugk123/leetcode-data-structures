from typing import List
class Solution:
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