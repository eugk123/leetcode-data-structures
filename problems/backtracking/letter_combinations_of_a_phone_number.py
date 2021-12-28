"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
<view image on leetcode>

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

:type digits: str
:rtype: List[str]
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Algorithm: Backtracking

        Backtracking is an algorithm for finding all solutions by exploring all potential candidates.
        If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards
        it by making some changes on the previous step, i.e. backtracks and then try again.

                                2
                            /   |   \
                          a     b     c
                        /       |       \
                        3       3       3
                      / | \   / | \   / | \
                     d  e  f d  e  f d  e  f
                     |  |  | |  |  | |  |  |
                    ad ae af bd be bf cd ce cf
        """

        # Initialize numpad as HashMap
        num_pad = dict()
        num_pad['0'] = None
        num_pad['1'] = None
        num_pad['2'] = 'abc'
        num_pad['3'] = 'def'
        num_pad['4'] = 'ghi'
        num_pad['5'] = 'jkl'
        num_pad['6'] = 'mno'
        num_pad['7'] = 'pqrs'
        num_pad['8'] = 'tuv'
        num_pad['9'] = 'wxyz'

        # Store results here
        combinations = []

        # Take all combinations of input digits from left to right (no reverse)
        # index -> current index, combination -> current combination
        def dfs(index, combination):

            # When index is equal len(digits), we know we've reached the end
            if index == len(digits):
                combinations.append(combination)
                return

            # Grab current digit and set of letters.
            digit = digits[index]
            letters = num_pad.get(digit)

            # Iterate through each letter then perform DFS to traverse next digit (thus adding another letter)
            for letter in letters:
                # No need to update the string by removing the letter because strings are immutable.
                # This means in the next recursive call using a different letter, the old state will not be saved!
                dfs(index + 1, combination + letter)

        if digits == "":
            return []

        dfs(0, "")
        return combinations

    def letterCombinationsChar(self, digits: str) -> List[str]:
        """
        https://www.youtube.com/watch?v=nNGSZdx6F3M&list=PLujIAthk_iiO7r03Rl4pUnjFpdHjdjDwy&index=1&t=167s
        """
        # Store our answers
        result = []

        # Define map
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if digits is not [] and len(digits) > 0:
            self.dfs(digits, phone, result, [], 0)
        return result

    def dfs(self, digits, phone, result, string_list, index):
        # Base Case (one digit)
        if len(digits) == 1:
            for letter in phone[digits]:
                result.append(letter)
            return

        # Closure Condition: Reached end of phone number (digits), we should have a valid letter combination
        if index == len(digits):
            # Join letters to from combination
            string = "".join(string_list)
            result.append(string)
            return

        # If there are digits to check, grab letters using digit
        letters = phone[digits[index]]

        for letter in letters:
            string_list.append(letter)  # Make changes -> Add letter
            print(string_list)
            self.dfs(digits, phone, result, string_list, index + 1)  # Take first letter, and traverse to next digit via index (send search party)
            string_list.pop()  # Backtrack and revert changes -> Removes previous letter (This allows us to try other options.)

if __name__ == '__main__':
    print(Solution().letterCombinationsChar("23"))
