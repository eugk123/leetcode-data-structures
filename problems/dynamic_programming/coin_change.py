"""
https://leetcode.com/problems/coin-change/
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(current):
            # MEMO Get
            if current in memo:
                return memo.get(current)

            # only return when current reaches amount
            if current == amount:
                return 0

            # try all paths, only when current < amount: 
            ans = math.inf
            if current < amount:
                for coin in coins:
                    # take the minimum of all paths
                    ans = min(ans, 1 + dfs(current + coin))

            # MEMO Update
            memo[current] = ans
            
            return ans

        memo = {}
        cost = dfs(0)
        
        # if no cost is found, we know cost is still math.inf
        if cost != math.inf:
            return cost
        return -1

    def coinChangeTLE(self, coins: List[int], amount: int) -> int:
        def dfs(current):
            # only return when current reaches amount
            if current == amount:
                return 0

            # try all paths, only when current < amount: 
            ans = math.inf
            if current < amount:
                for coin in coins:
                    # take the minimum of all paths
                    ans = min(ans, 1 + dfs(current + coin))
            
            return ans

        cost = dfs(0)
        
        # if no cost is found, we know cost is still math.inf
        if cost != math.inf:
            return cost
        return -1

        
if __name__ == '__main__':
    print(Solution().coinChange(coins=[1,2,5], amount=100))
    # print(Solution().coinChangeGivenCoins(amount=100))