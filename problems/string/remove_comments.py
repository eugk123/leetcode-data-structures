"""
https://leetcode.com/problems/remove-comments
"""
from typing import List
class Solution:
    """

    Time Complexity - O(S) where S is total length of string
    Space Complexity - O(S) where S is total length of string and recorded in the result array.
    """
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False  # We need a boolean to check if we're in a block comment /*. */

        # We will have to iterate line by line
        for line in source:

            # If we're still in a block comment, we want to keep it all in one line.
            # If we're not in a block comment, then we can add the line to result and reset for next line.
            if not in_block:
                res_current_line = []

            i = 0

            # A while loop is required for this due to the need for skipping iterations twice for block comments
            while i < len(line):
                # If prev and current letter is "/" and "*" respectively, stop writing until prev and current letter is "/" and "*" respectively
                # This is possible by turning the switch to True
                # We also need to stop writing when index i is set at "/"
                # Added "block_comment_switch == True" to skip when in block comments
                if i < len(line) - 1 and line[i] == "/" and line[i + 1] == "*" and not in_block:
                    in_block = True
                    i += 1

                elif i < len(line) - 1 and line[i] == "*" and line[i + 1] == "/" and in_block == True:
                    in_block = False
                    i += 1

                # If prev and current letter is "/". skip the rest of the letters in this line
                # Added "block_comment_switch == True" to skip when in block comments
                elif i < len(line) - 1 and line[i] == "/" and line[i + 1] == "/" and not in_block:
                    break

                # Constantly write letter to result if we're not in the block comment (/* */)
                elif in_block == False:
                    letter = line[i]
                    res_current_line.append(letter)
                i += 1

            # If we're still in a block comment, we want to keep it all in one line.
            # If we're not in a block comment, then we can add the line to result and reset for next line.
            if not in_block:

                new_line = "".join(res_current_line)
                if not new_line == "":
                    result.append(new_line)
        return result