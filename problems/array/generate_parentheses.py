"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import List
class Solution():
    """
    https://www.youtube.com/watch?v=N-3fyoKD8-k
    For faster computation for building a string, use a list of characters. In this case, the speed is not changed much
    due to the tight restrictions on string length.

    When performing backtracking for a mutable object such as a list, you'll need to reverse it to allow for other options.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            # If len(S) exceeds len(2 * n), append result then return
            if len(S) == 2 * n:
                combo = ''.join(S)
                ans.append(combo)
                return

            # If the # of open paren is less than input n
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()

            # If the # of close paren is less than # of open paren
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack()
        return ans

    def generateParenthesisString(self, n: int) -> List[str]:
        """
        String is immutable. Therefore when backtracking,
        the referenced string is in it's original state when passed to the next recursive method.
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            # If len(S) exceeds len(2 * n), append result then return
            if len(S) == 2 * n:
                # combo = ''.join(S)
                ans.append(S)
                return

            # If the # of open paren is less than input n
            if left < n:
                backtrack(S + '(', left+1, right)

            # If the # of close paren is less than # of open paren
            if right < left:
                backtrack(S + ')', left, right+1)

        backtrack()
        return ans
if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

    # ['((()))', '(()())', '(())()', '()(())', '()()()']