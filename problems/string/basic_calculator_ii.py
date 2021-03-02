"""
https://leetcode.com/problems/basic-calculator-ii
"""
class Solution:
    def calculate(self, s: str) -> int:
        # Initialize stack and current_number
        stack = []
        current_number = 0

        # Initialize operator (This is the first part of the loop)
        operator = "add"

        for i in range(len(s)):
            char = s[i]

            # Skip if space (but in case the last letter is space, you want to keep that so it processes the final number)
            if char == " " and i < len(s) - 1:
                continue

            # 1. Get current number
            if char.isnumeric():
                current_number = 10 * current_number + int(char)

            # 2. When it is an operator or end is reached, use the previous operator to do the following:
            if not char.isnumeric() or i == len(s) - 1:
                # 2a. +,- -> Add to stack
                if operator == "add":
                    stack.append(current_number)
                elif operator == "subtract":
                    stack.append(-current_number)

                # 2b. *,/ -> Update top element
                elif operator == "multiply":
                    stack[len(stack) - 1] = stack[len(stack) - 1] * current_number
                elif operator == "divide":
                    stack[len(stack) - 1] = int(stack[len(stack) - 1] / current_number)
                current_number = 0

            # print(i, current_number, stack)

            # 3. Update next operator
            if s[i] == '+':
                operator = "add"
            elif s[i] == '-':
                operator = "subtract"
            elif s[i] == '*':
                operator = "multiply"
            elif s[i] == '/':
                operator = "divide"

                # Initialize result
        res = 0
        for num in stack:
            res = res + num

        return res