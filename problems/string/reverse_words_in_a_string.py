"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
from collections import deque
class Solution:
    """
    Build word char by char. Append to Queue on left side. Make sure to skip duplicate, leading, and trailing spaces.
    """
    def reverseWordsEugene(self, s: str) -> str:
        """
        Hooray! I did a new solution a bit more concise than the given solution with the same O(N) time & space.
        """
        # Add each word to queue by appending left at space or reaching end.
        word = ""  # Initialize empty word
        queue = deque()  # Use queue to store each word to return in reverse.
        count = 0  # Keep track of length
        for letter in s:
            count += 1

            # If space, (1) word is not empty, add to queue and (2) skip
            if letter == " ":
                if word:
                    queue.appendleft(word)
                    word = ""
                continue

            # For the final letter in case it's not a space, you need to also add it to the word and append the word to queue!
            elif count == len(s):
                word += letter  # Make sure to add the last letter!
                queue.appendleft(word)

            word += letter

        return " ".join(queue)

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
    print(Solution().reverseWordsEugene('  a  b b  '))