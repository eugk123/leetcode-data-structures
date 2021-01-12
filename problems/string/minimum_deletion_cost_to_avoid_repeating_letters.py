"""
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
"""
from typing import List
class Solution:
    """
    Hint 1: When checking for identical characters, check the previous instead of the next.
    Hint 2: When getting the total cost of repeating characters, take the total sum and subtract by the max

    https://www.youtube.com/watch?v=3zMxJJxYph4
    """
    def minCost(self, s: str, cost: List[int]) -> int:
        group_sum = group_max = ans = 0

        for i in range(len(s)):
            # Constraint - Resetting the sums when previous character is different
            if i > 0 and s[i] != s[i - 1]:
                ans += group_sum - group_max
                group_sum = group_max = 0

            # Get the sum of all the indices except for when the constraint is applied
            group_sum = group_sum + cost[i]
            group_max = max(group_max, cost[i])

        # The final repeats are not captured
        ans += group_sum - group_max
        return ans

if __name__ == '__main__':
    print(Solution().minCost(s='aaabbb',
                             cost=[3,5,1,2,3,4]))