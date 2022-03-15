"""
https://leetcode.com/problems/basic-calculator/submissions/
"""
class Solution:
    """
    
    """
    def calculate(self, s: str) -> int:
        
        stack = []
        
        for letter in s:
            # if open paren,
            if letter == " ":
                continue
                
            if letter == "(" or letter == "+" or letter == "-":
                stack.append(letter)
                continue
            
            # for numbers with multiple digits, we need to update the previous number in stack
            if letter.isnumeric():
                if stack:
                    if stack[len(stack) - 1].isnumeric():
                        stack.append(stack.pop() + letter)
                    else:
                        stack.append(letter)
                else:
                    stack.append(letter)

                
            if letter == ")":
                # we're going to sum up the numbers until the open paren is found
                # once open paren is found, we sum up numbers then add back to stack
                # "1","-","(","1","+","1" -> 1 + 1 = 2
                # "1","-","2"
                total = curr = 0
                while stack[len(stack) - 1] != "(":
                    if stack[len(stack) - 1] == "+": 
                        stack.pop() 
                        curr = curr
                        total = total + curr
                    elif stack[len(stack) - 1] == "-":
                        stack.pop() 
                        curr = -curr
                        total = total + curr
                    else:
                        curr = int(stack.pop())
                    
                    # Break out if open paren is found, remove that open paren, then add back total
                    if stack[len(stack) - 1] == "(":
                        stack.pop()  # pop '('
                        if curr < 0:
                            break
                        total = total + curr
                        break

                stack.append(total)
        print(stack)
        total = curr = 0
        # sum up in reverse to simply handle negatives.
        for ele in reversed(stack):
            if ele == "+":
                total = total + curr
            elif ele == "-":
                total = total - curr
            else:
                curr = int(ele)
                
        if stack[0] == "-":
            return total
        else:
            return total + curr