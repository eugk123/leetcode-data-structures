"""
https://leetcode.com/problems/min-stack/
"""
class MinStack:
    """
    O(1) time complexity across all operations.

    Need 2nd stack to achieve O(1) time on getMin(). 2nd stack will hold all minimum values.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        # If stack empty or x is less than minValue, populate in minStack.
        # minValue is found at the end of the minStack.
        if not self.stack or x <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(x)

            # Always populate the original stack
        self.stack.append(x)

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.minStack[len(self.minStack) - 1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[len(self.minStack) - 1]