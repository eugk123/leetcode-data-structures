"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""
import math
from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Work backwards - way easier.
        prev = math.inf
        for i in reversed(range(len(arr))):
            # First index -> store as prev and replace with -1
            if i == len(arr) - 1:
                prev = arr[i]
                arr[i] = -1

            # Rest of indices, check if curr > prev, if true update prev (use a temp pointer) and replace with prev.
            # Else, just replace with prev
            elif arr[i] > prev:
                temp = arr[i]
                arr[i] = prev
                prev = temp
            else:
                arr[i] = prev

        return arr