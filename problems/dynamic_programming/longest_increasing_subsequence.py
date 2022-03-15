"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List
class Solution:
    """
    Top-down Memo 1D

    Time O(N^2)
    Space O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(index, prev):
            # MEMO Get
            if index in memo:
                return memo.get(index)
            
            # end reached, don't count
            if index >= len(nums):
                return 0
            
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
        return dfs(0, -math.inf)

if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[1,2,3,4]))