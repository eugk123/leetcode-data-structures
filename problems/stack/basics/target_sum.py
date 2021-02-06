"""
https://leetcode.com/problems/target-sum/
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        See below for just using DFS resulting in TLE.

        This solution is DFS with memoization
        https://leetcode.com/problems/target-sum/discuss/325250/Python-different-soluctions%3A-DFS-BFS-DP

        We add memorization to get rid of duplicate calls.

        Time complexity: O(l⋅n). The memo array of size l⋅n has been filled just once.
            Here, l refers to the range of sum. n refers to the size of nums array.
        Space complexity: O(l⋅n). The depth of recursion tree can go up to n. The memo array contains l⋅n elements.
        """

        def dfs(current, index):
            # If current is found in memo, return cached value
            if (current, index) in memo:
                return memo.get((current, index))

            # Constraint: if end is reached, return
            if index == len(nums):

                # Constraint: target is reached, +1
                if current == S:
                    return 1
                else:
                    return 0

            # if (current, index) not in memo:

            add = dfs(current + nums[index], index + 1)
            minus = dfs(current - nums[index], index + 1)
            memo[(current, index)] = add + minus

            return add + minus

        # Use memorization to reduce number of duplicate results coming from recursive calls
        # Use tuple of (sum, index)
        # Example duplicate call: (2,2) = -1 1 = 1 -1
        memo = {}

        # Start at sum = 0 and index = 0
        return dfs(0, 0)

    def findTargetSumWays_DFS_TLE(self, nums: List[int], S: int) -> int:
        """
        Time limit exceeded with just DFS.

        Time complexity: O(2^n) - size of recursion tree, n refers to the size of the nums array
        Space complexity: O(n) - depth of recursion tree
        """

        def dfs(current, index):
            # Constraint: if end is reached, return
            if index == len(nums):

                # Constraint: target is reached, +1
                if current == S:
                    self.count += 1
                return

            dfs(current + nums[index], index + 1)
            dfs(current - nums[index], index + 1)

            return self.count

        # You will take every possible combination and count every time when
        # the sum == target and the index goes beyond the last digit
        self.count = 0

        # Start at sum = 0 and index = 0
        return dfs(0, 0)

if __name__ == '__main__':
    print(Solution().findTargetSumWays(nums=[1,1,1,1,1],S=3))
    print(Solution().findTargetSumWays_DFS_TLE(nums=[1,1,1,1,1],S=3))
