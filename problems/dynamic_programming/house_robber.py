"""
https://leetcode.com/problems/house-robber/
"""
from typing import List
class Solution:
    """
    Top-down Memo 1D

    Maximum cost. 
    - Out of bounds return: 0
    - End of array return: current cost
    - End return: maximum of paths max(a, b)

    O(n) Time - len of cache
    O(n) Space - len of cache
    """
    def rob(self, nums: List[int]) -> int:
        """
        1238
        x x 
        x  x

        """
        def dfs(index):
            if index in memo:
                return memo.get(index)
            
            # out of bounds, add 0
            if index == len(nums):
                return 0

            # at last index, add sum
            if index == len(nums) - 1:
                return nums[index]
            
            
            a = dfs(index + 1)  # skip current index to add later, like 3 spaces away
            b = nums[index] + dfs(index + 2)  # skip 2 indices and rob
            memo[index] = max(a, b)
            return max(a, b)
        
        memo = {}
        return dfs(0)

    def rob2(self, nums: List[int]) -> int:
        """
        Alternatively, instead of starting at all indices, just skip 2 and skip 3
        """
        def dfs(index):
            if index in memo:
                return memo.get(index)
            
            if index >= len(nums):
                return 0
            if index == len(nums) - 1:
                return nums[index]
            
            # skip 1 house
            a = nums[index] + dfs(index + 2)

            # skip 2 houses
            b = nums[index] + dfs(index + 3)
            
            memo[index] = max(a, b)
            
            return max(a, b)
        
        memo = {}        
        return max(dfs(0), dfs(1))

    def robTLE(self, nums: List[int]) -> int:
        
        def dfs(index):
            if index >= len(nums):
                return 0
            if index == len(nums) - 1:
                return nums[index]
            
            # skip 1 house
            a = nums[index] + dfs(index + 2)

            # skip 2 houses
            b = nums[index] + dfs(index + 3)
                        
            return max(a, b)
        
        return max(dfs(0), dfs(1))