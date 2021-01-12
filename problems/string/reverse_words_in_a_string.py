"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
from collections import deque
class Solution:
    """
    Build word char by char. Append to Queue on left side. Make sure to skip duplicate, leading, and trailing spaces.
    """
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1

        # remove leading spaces
        while s[left] == ' ':
            left += 1

        # remove trailing spaces
        while s[right] == ' ':
            right -= 1

        word = []  # This will be used to collect each character to build your word
        queue = deque()  # This will be used to populate your result. The trick is to append word by word on the left.
        for i in range(left, right + 1):
            # Populate word whenever no space
            if s[i] != ' ':
                word.append(s[i])

            # Pushing word to queue when end is reached
            if i == right:
                queue.appendleft(''.join(word))
                word = []

            # Drop duplicate spaces (But requires a conditional at i == right, otherwise this will fail)
            elif s[i] == ' ' and s[i + 1] == ' ':
                continue

            # Pushing word to queue (same duplicate code. can't figure out a way around this)
            elif s[i] == ' ':
                queue.appendleft(''.join(word))
                word = []

        return ' '.join(queue)  # This effectively builds your string separated by spaces


if __name__ == '__main__':
    print(Solution().reverseWords('  a  b b  '))