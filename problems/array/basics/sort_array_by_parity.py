"""
https://leetcode.com/problems/sort-array-by-parity/
"""
from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # Two Pointer from edges. Have even numbers followed by odd

        # If left points to odd, swap left and right
        left, right = 0, len(A) - 1
        while left < right:
            # While right is odd, traverse
            while int(A[right] % 2) == 1:
                right -= 1
                if right < 0:
                    break
                elif right == left:
                    break

            # Now right is definitely even, when left is odd, swap.
            if int(A[left] % 2) == 1 or A[left] == 1:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
            left += 1

        return A