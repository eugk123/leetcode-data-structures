"""
https://leetcode.com/problems/subsets/
"""
from typing import List
class Solution:
    """
    O(N*2^n) Time Complexity. This is difficult to calculate. You need to follow this approach!
    https://leetcode.com/problems/subsets/discuss/634416/Time-complexity-backtrack-solution-my-detailed-derivation
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        The approach here is very similar to 1239. Maximum Length of a Concatenated String with Unique Characters
        https://jamboard.google.com/d/1JMV60IvmTvqvcyf6dyc7bFG-VL0LDadsDia5xtwC8gk/viewer?f=0

        Notice you want to take all possible combinatinos starting at every index.
        You only traverse towards the right. Hence, the traversal range starts at current index instead of zero.
        """
        def dfs(index):
            # Constraint - already exists
            if subset in res:
                return

            # Add to result
            # Copy allows for updating the currenting result. Otherwise it'll mutate backwards.
            res.append(subset.copy())

            # Constraint - out of bounds
            if index == len(nums):
                return

            # Traverse to the right - start at current index not 0
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

            return


        subset = []
        res = []
        dfs(0)
        return res