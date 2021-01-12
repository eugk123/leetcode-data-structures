"""
https://leetcode.com/problems/minimize-rounding-error-to-meet-target/
"""
from math import floor, ceil
from typing import List
class Solution:
    """
    https://leetcode.com/problems/minimize-rounding-error-to-meet-target/discuss/879183/python-greedy-clean-solution-with-DETAILED-explanation-beat-100!!!!
    """
    def minimizeError(self, prices: List[str], target: int) -> str:  # Heapsort
        total_floor = total_ceil = res = 0
        sorted_prices = []  # This will be your sorted array

        for price in prices:
            p = float(price)
            total_ceil += ceil(p)
            total_floor += floor(p)  # We will need the total floor price for optimization.
            sorted_prices.append(p - floor(p))  # Subtract floor price. We only care about the decimal place when getting the result.

        # Sort in ascending order after subtracting floor price
        sorted_prices.sort()

        # The optimal number of floors and ceils are determined with the total_floor, len(prices), and target
        n_floor = total_floor + len(prices) - target
        n_ceil = len(prices) - n_floor

        # If target exceeds total_floor + len(prices) or falls below total_floor, then return "-1"
        if target > total_ceil or target < total_floor:
            return "-1"
        for price in sorted_prices:
            diff_floor = diff_ceil = 0
            # Since it's sorted in ascending order, we grab floor diffs first. Then ceil after floors diffs are done.
            if n_floor != 0:
                diff_floor = price - floor(price)
                n_floor -= 1
            elif n_ceil != 0:
                diff_ceil = ceil(price) - price
                n_ceil -= 1
            res = res + max(diff_ceil, diff_floor)
        return "{:.3f}".format(res)

if __name__ == '__main__':
    print(Solution().minimizeError(prices=["2.000","2.000","2.000","2.000","2.000"], target=11))
