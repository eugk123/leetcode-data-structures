"""
https://leetcode.com/problems/daily-temperatures/
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=WGm4Kj3lhRI

    Work backwards and store
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []  # Use stack to collect the hottest temperatures.
        res = [0] * len(T)  # Initialize result and update as you iterate

        # Reversing makes it possible for O(N) since you can store hottest days in the stack.
        # Store last index in stack. Result is 0.
        last_index = len(T) - 1
        stack.append((T[last_index], last_index))

        for i in reversed(range(len(T) - 1)):

            # If next number is less, add to stack. Set result to 1.
            if T[i] < stack[len(stack) - 1][0]:
                stack.append((T[i], i))
                res[i] = 1

            # Otherwise, keep popping if popped value is less than current.
            else:
                while stack:
                    val, index = stack.pop()
                    if T[i] >= val:
                        continue
                    else:
                        # Put it back into the stack because we know this val is greater than current element
                        stack.append((val, index))
                        break

                # If stack is empty, we know current value is the greatest. Set result to 0 and append.
                if not stack:
                    res[i] = 0

                # Update result for current index.
                else:
                    res[i] = index - i

                stack.append((T[i], i))

        return res