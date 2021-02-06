"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # First pass: add K=val/2, V=index to HashMap only for even numbers - we can rule out odds.
        map = dict()
        count_zeroes = count_ones = 0
        for i in range(len(arr)):
            # Edge case 0 or 1
            if arr[i] == 0:
                count_zeroes += 1
                if count_zeroes == 2 or count_ones == 2:
                    return True
                continue
            if arr[i] == 1:
                count_ones += 1
                if count_zeroes == 2 or count_ones == 2:
                    return True
                continue

            # Even numbers, add to map - ignore odds
            if arr[i] % 2 == 0:
                map[int(arr[i] / 2)] = i

        # Second pass: we check if value is in HashMap then return the index if met.
        for num in arr:
            if map.get(num) is not None:
                return True
        return False