"""\
https://leetcode.com/problems/coin-change-2
"""
class Solution:
    """
    https://leetcode.com/problems/coin-change-2/discuss/675862/Python-or-Top-Down-DP

    Total unique paths -> return 1 or 0 on boundary conditions, do not count on dfs() calls.

    The tricky part here is that the coins need to be sorted in descending order for optimizing time.
        Sorting is to ensure that the larger coins are considered first, and in the subsequent sub-braches of the recursion, 
        we don't consider the bigger elements (notice enumeration is restricted to coins[index:]). 
        This way we don't get duplicate combinations (for e.g for 4 [1,2,1] and [2,1,1] are the same.
        By sorting and considering 2 first, you don't get the [1,2,1] possibility at all).
    
    Time & Space O(n*amount)
    """
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(index, current):
            # looking for total unique paths
            # we return 1/0 on the boundary
            if current == amount:
                return 1
            if current > amount:
                return 0

            if (index, current) in memo:
                return memo.get((index, current))

            # summing up all possible paths
            ans = 0
            for i in range(index, len(coins)):
                ans = ans + dfs(i, current + coins[i])
        
            memo[(index, current)] = ans
            return ans
        
        coins.sort(reverse=True)
        memo = {}
        
        return dfs(0, 0)