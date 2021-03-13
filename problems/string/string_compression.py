"""
https://leetcode.com/problems/string-compression/
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=IhJgguNiYYk

    LeetCode not only wants the len(string), but also the modified input array.

    My solution below differs, but still achieves best possible solution!
    O(n) time and O(1) space.
    """
    def compress(self, chars: List[str]) -> int:
        count = 1  # Use count to count have many repeating characters
        index = 1  # Use index for updating the chars array
        prev = chars[0]
        for char in chars[1:]:

            # Same character, add count
            if char == prev:
                count += 1

            # Different character, reset count to 1
            if char != prev:
                # Depending on how many digits, will determine how many iterations to pass along with the number
                # of characters to replace with each digit
                # ex: count == 120 -> "1", "2", "0", skip i (3 times)
                if count > 1:
                    for num in str(count):
                        chars[index] = num
                        index += 1

                count = 1  # Reset count

                # Since different character is found, we need to update the next index with that new character.
                # Do not forget to traverse everytime you update an index in the array.
                chars[index] = char
                index += 1
            prev = char

        # The way this algorithm works is it checks for a difference between current and previous character.
        # So you need to treat the end as a different character and run this count loop one more time to add
        # the number to the chars array.
        if count > 1:
            for num in str(count):
                chars[index] = num
                index += 1

        # Finally, the remainder of the char array can be trimmed out.
        for i in range(index, len(chars)):
            chars.pop()

        # Return the total length as the result
        return len(chars)
if __name__ == '__main__':
    print(Solution().compress(chars=["a","a","v"]))

