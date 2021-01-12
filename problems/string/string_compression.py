"""
https://leetcode.com/problems/string-compression/
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=IhJgguNiYYk

    LeetCode not only wants the len(string), but also the modified input array.

    Better solution in video. Below is my solution.
    """
    def compress(self, chars: List[str]) -> int:
        # Base Case - len(chars) == 1 -> return 1
        if len(chars) == 1:
            return 1

        # Two pointer solution. Traverse with right pointer.
        # Bring left pointer when there is a new character
        string = ''
        left = 0
        # As you move right, keep checking the previous element to see if it's the same character
        for right in range(len(chars)):
            # Check final index to see if it's the same as the previous index.
            # When same, traverse till end
            # FINAL INDEX CHECK MUST BE BEFORE THE GENERAL CASE. Otherwise this final index check will never be reached.
            if right == len(chars) - 1 and chars[right] == chars[right-1]:
                count = 0
                while left < right:
                    left += 1
                    count += 1
                string += chars[right]
                string += str(count + 1)
                continue
            # When different, just add character
            elif right == len(chars) - 1 and chars[right] != chars[right-1]:
                count = 0
                while left < right:
                    left += 1
                    count += 1
                string += chars[right - 1]
                if count > 1:
                    string += str(count)
                string += chars[right]
                continue


            # All other indices, check if first and previous index are the same.
            if right > 0 and chars[right] == chars[right-1]:
                continue
            elif right > 0 and chars[right] != chars[right - 1]:
                count = 0
                # Traverse left pointer and count until chars[left] == chars[right]
                while chars[left] != chars[right]:
                    left += 1
                    count += 1
                string += chars[right - 1]
                if count > 1:
                    string += str(count)

        # Need to pop the rest of the chars elements:
        for i in range(len(string)):
            print(string[i])
            chars[i] = string[i]
        for i in range(len(string), len(chars)):
            chars.pop()
        return len(string)

if __name__ == '__main__':
    print(Solution().compress(chars=["a","a","v"]))

