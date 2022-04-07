"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List
class Solution:
    """
    Top-down Memo 1D

    We try every combination using for loop (index, length). Consider a worst cast example of all increasing digits.
    We need to consider every possible combination.
    01234
    0     1
    01      ->  012, 01 3, 01  4
    0 2     ->  0 23, 0 2 4
    0  3    ->  0  34
    0   4

    Time O(N^2)
    Space O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(index, prev):
            # MEMO Get
            if index in memo:
                return memo.get(index)
            
            # past end, don't count. 
            # Why not index == len(nums)-1 return 1? Can't because at the end, sometimes nums[i] is not > prev! So we don't want to count all the end occurences.
            if index >= len(nums):
                return 0
            
            # ALL our paths are from LEFT to RIGHT. Start at every index.
            # Similar to how we solve subsets and combination sums, we use for loop from (index, len) to start our path at every index.
            ans = 0
            for i in range(index, len(nums)):
                # only when next number is greater than previous, we add
                if nums[i] > prev:
                    ans = max(ans, 1 + dfs(i, nums[i]))
            
            # MEMO Add
            memo[index] = ans
            return ans
        
        if len(nums) == 1:
            return 1
        
        # MEMO Init
        memo = {}

        # We initialize prev to -inf because we want to count the first iteration
        return dfs(0, -math.inf)

if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[1,2,3,4]))