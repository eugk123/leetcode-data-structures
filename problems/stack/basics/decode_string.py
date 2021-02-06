"""
https://leetcode.com/problems/decode-string/
"""
import time
class Solution:
    def decodeString(self, s: str) -> str:
        # For optimal time, you must use an array of characters then join in the end

        # Scenario 2: 2[a2[b]c]
        # ['2','[','a','2','[','b'

        # When ']' is reached, pop() until '['

        stack = []  # [num, string]
        result = ""
        numbersCombined = lettersCombined = ""
        for i in range(len(s)):

            # If close bracket is reached, collect letters, duplicate based on most recent number,
            # From here if stack is empty, then we can add to result because there are no more other brackets
            # Otherwise, add back into stack and keep adding until next close bracket is reached.
            if s[i] == "]":
                lettersCombined = letters = ""  # Reset combined letters

                # When ']' is reached, pop() until '['
                while stack[len(stack) - 1] != "[":
                    letters = stack.pop() + letters
                stack.pop()  # Remove '['
                number = int(stack.pop())  # Get multiplier

                # Duplicate letters based on multiplier
                for _ in range(number):
                    lettersCombined += letters

                if stack:
                    stack.append(lettersCombined)
                else:
                    result = result + lettersCombined

            # Need to be able to combine numbers before adding it to the stack
            elif s[i].isnumeric():
                numbersCombined = numbersCombined + s[i]

            # Since '[' happens at the end of the number, we can combine it then
            elif s[i] == '[':
                stack.append(numbersCombined)  # Add combined number
                stack.append('[')  # Add '[' or s[i] same thing
                numbersCombined = ""  # Reset combined numbers

            # Add to stack for all characters when stack is not empty. Above conditions take care of numbers, '[', ']'
            elif stack:
                stack.append(s[i])

            # Only adding characters to result that are outside brackets!
            else:
                result = result + s[i]

        return result

    def decodeStringCharArray(self, s: str) -> str:
        # For optimal time, you must use an array of characters then join in the end

        # Scenario 2: 2[a2[b]c]
        # ['2','[','a','2','[','b'

        # When ']' is reached, pop() until '['

        stack = []  # [num, string]
        result = []
        numbersCombined = lettersCombined = ""
        for i in range(len(s)):

            # If close bracket is reached, collect letters, duplicate based on most recent number,
            # From here if stack is empty, then we can add to result because there are no more other brackets
            # Otherwise, add back into stack and keep adding until next close bracket is reached.
            if s[i] == "]":
                lettersCombined = letters = ""  # Reset combined letters

                # When ']' is reached, pop() until '['
                while stack[len(stack) - 1] != "[":
                    letters = stack.pop() + letters
                stack.pop()  # Remove '['
                number = int(stack.pop())  # Get multiplier

                # Duplicate letters based on multiplier
                for _ in range(number):
                    lettersCombined += letters

                if stack:
                    stack.append(lettersCombined)
                 else:
                    result.append(lettersCombined)

            # Need to be able to combine numbers before adding it to the stack
            elif s[i].isnumeric():
                numbersCombined = numbersCombined + s[i]

            # Since '[' happens at the end of the number, we can combine it then
            elif s[i] == '[':
                stack.append(numbersCombined)  # Add combined number
                stack.append('[')  # Add '[' or s[i] same thing
                numbersCombined = ""  # Reset combined numbers

            # Add to stack for all characters when stack is not empty. Above conditions take care of numbers, '[', ']'
            elif stack:
                stack.append(s[i])

            # Only adding characters to result that are outside brackets!
            else:
                result.append(s[i])

        return "".join(result)


if __name__ == '__main__':

    t = time.process_time()
    Solution().decodeString(s='400[aaaaaaaaaaaaaaaaa300[bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb]40[ccccccccccccccc]]')
    elapsed_time = time.process_time() - t

    t_prime = time.process_time()
    Solution().decodeStringCharArray(s='400[aaaaaaaaaaaaaaaaa300[bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb]40[ccccccccccccccc]]')
    elapsed_time_prime = time.process_time() - t_prime

    # When comparing string concatenation vs using a list, the time seems the same.
    print("Decode String using String Concatenation:", elapsed_time)
    print("Decode String using Char Array:", elapsed_time_prime)
