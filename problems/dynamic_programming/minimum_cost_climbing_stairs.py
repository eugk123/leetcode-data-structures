"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""
class Solution:
    """
    Top-down Memo 1D

    Minimum Cost. 
    - Out of bounds return: 0
    - End of array return: current cost
    - End return: minimum of paths min(a, b)
    
    Time & Space O(N) size of cache
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        def dfs(index):    
            # MEMO Get   
            if index in memo:
                return memo.get(index)

            # out of bounds, return 0
            if index >= len(cost):
                return 0

            # cost continues to add up until end is reached
            if index == len(cost) - 1:
                return cost[index]
            
            # one step
            a = cost[index] + dfs(index + 1)
            
            # two step
            b = cost[index] + dfs(index + 2)
            
            # MEMO Update
            memo[index] = min(a,b)
            return min(a, b)
            
        # MEMO Init
        memo = {}

        # remember, you want to start at index 0 or 1
        return min(dfs(0), dfs(1))

    def minCostClimbingStairsTLE(self, cost: List[int]) -> int: 
        def dfs(index):       
            # out of bounds, return 0
            if index >= len(cost):
                return 0

            # cost continues to add up until end is reached
            if index == len(cost) - 1:
                return cost[index]
            
            # one step
            a = cost[index] + dfs(index + 1)
            
            # two step
            b = cost[index] + dfs(index + 2)
            
            return min(a, b)
            
        # remember, you want to start at index 0 or 1
        return min(dfs(0), dfs(1))