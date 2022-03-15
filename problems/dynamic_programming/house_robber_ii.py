"""
https://leetcode.com/problems/house-robber-ii
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(index, is_last_available):
            if index in memo:
                return memo.get(index)
            
            if index >= len(nums):
                return 0
            
            if index == len(nums) - 1:
                if is_last_available:
                    return nums[index]
                else:
                    return max(0, nums[index] - nums[0])
            
            # try every index
            a = dfs(index + 1, is_last_available)

            # from each path, add current cost and skip to next house.
            b = dfs(index + 2, is_last_available) + nums[index]
            
            memo[index] = max(a,b)
            
            return max(a, b)
        
        # return(dfs(0, False))
        if len(nums) == 1:
            return nums[0]
        
        # return max(dfs(0, False), dfs(1, True))
        memo = {}
        a = dfs(0, False)

        memo = {}
        b = dfs(1, True)
        return max(a,b)
            