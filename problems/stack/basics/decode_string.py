"""
https://leetcode.com/problems/decode-string/
"""
import time
class Solution:
    """
    Stack

    Scenarios:
    1. Simple, 2[a]3[b] -> aabbb,
    2. Nested, 2[a3[b]] -> 2[abbb] -> abbbabbb,
    3. Nested + outer, z2[a3[b]]z -> zabbbabbbz
    4. Multiple digits, 20[abc] -> abcabcabc...

For each iteration, keep adding to stack until you reach "]". When you reach "]" continuously pop from stack and
build a string of letters until you reach "[". Once "[" is reached, skip "[" and pop again to retrieve the multiplier
in int(). Then update letters with letters*multiplier. Now if stack is empty, we know this isn't a nested scenario,
so we can append letters to result. If not empty, then add back to stack and continue!

Scenario 3 shows the possibility of having characters outside of the stack. To handle this, make sure to append to
result only when stack is empty.

Scenario 4 shows the possibility of having multiple digit multipliers. Make sure to update the multiplier and put
into stack as the FULL number.

    Time Complexity: O(maxK^(countK)*n) where maxK is the maximum value of k, countK is the count of nested k values
    and n is the maximum length of encoded string.

    Example: for s = 20[a10[bc]], maxK is 20, countK is 2 as there are 2 nested k values (20 and 10). Also, there are
    2 encoded strings a and bc with maximum length of encoded string, n as 2

    Example 2: for, s = 10[ab10[cd]]10[ef], time complexity would be roughly equivalent to
    10*{cd} * 10*{ab} + 10*2 = 10^2 * 2
2
 ∗2.
    """
    def decodeString(self, s: str) -> str:
        # For optimal time, you must use an array of characters then join in the end
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
        numbersCombined = ""
        for i in range(len(s)):

            # If close bracket is reached, collect letters, duplicate based on most recent number,
            # From here if stack is empty, then we can add to result because there are no more other brackets
            # Otherwise, add back into stack and keep adding until next close bracket is reached.
            if s[i] == "]":
                letters = ""  # Reset combined letters

                # When ']' is reached, pop() until '['
                while stack[len(stack) - 1] != "[":
                    letters = stack.pop() + letters
                stack.pop()  # Remove '['
                multiplier = int(stack.pop())  # Get multiplier

                if stack:
                    stack.append(multiplier*letters)
                else:
                    result.append(multiplier*letters)

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
    print(Solution().decodeString(s='2[ab2[cd]]'))
    print("\n")

    # Use a fat string for testing time complexity.
    s = '400[aaaaaaaaaaaaaaaaa300[bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb]40[ccccccccccccccc]]'

    # In python, you probably want to relay on using a list instead of string concatenation.
    # You must be thinking, wait the time is the same when i use string concatenation over the list. But this is not true.
    # In your case, it might be because of CPython's ability to reallocate pointers. But in most cases, it will be slower
    # See this reference https://stackoverflow.com/questions/34008010/is-the-time-complexity-of-iterative-string-append-actually-on2-or-on
    t = time.process_time()
    Solution().decodeString(s)
    elapsed_time = time.process_time() - t

    t_prime = time.process_time()
    Solution().decodeStringCharArray(s)
    elapsed_time_prime = time.process_time() - t_prime

    # When comparing string concatenation vs using a list, the time seems the same.
    print("Decode String using String Concatenation:", elapsed_time)
    print("Decode String using Char Array:", elapsed_time_prime)


    # Here is an example of string concatenation being slower than using a list of appended strings.
    t = time.process_time()
    new = ""
    s = "x"*100000
    for i in s:
        new = new + i
    elapsed_time = time.process_time() - t

    t_prime = time.process_time()
    new = []
    s = "x"*100000
    for i in s:
        new.append(i)
    new = "".join(new)
    elapsed_time_prime = time.process_time() - t_prime

    # When comparing string concatenation vs using a list, the time seems the same.
    print("String Concatenation:", elapsed_time)
    print("String Char Array:", elapsed_time_prime)