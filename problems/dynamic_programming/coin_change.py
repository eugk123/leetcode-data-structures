"""
https://leetcode.com/problems/coin-change/
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=H9bfqozjoqs&t=705s
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom Up Memoization Approach.

        See simplified problem using coins=[1,2,5] at coinChangeGivenCoins.
        The solution takes the simplified approach and converts it with coins as an input
        """
        # Initialize size of memo array, we add 1 to amount to account for base case dp[0]=0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            # We are storing index=TOTAL to dp[i]=NUMBER_OF_COINS
            # We are storing the number of coins. So when we add a penny, that's one more coin!
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        return -1


    def coinChangeGivenCoins(self, amount: int) -> int:
        """
        Given coins = [1, 2, 5], these are the step sizes of your problem.
        We can break down the problem into sub-problems as follows:

        Example amount = 100

                  f(100)
               /-1  |-2  \-5
            f(99) f(98) f(95)

        """
        # Initialize size of memo array, we add 1 to include amount = 0
        # index = total amount, value = number of coins
        dp = [0] * (amount + 1)

        for i in range(len(dp)):
            # We are storing index=TOTAL to dp[i]=NUMBER_OF_COINS
            # We are storing the number of coins. So when we add a penny, that's one more coin!
            if i >= 1:
                dp[i] = dp[i - 1] + 1

            if i >= 2:
                dp[i] = min(dp[i], dp[i - 2] + 1)

            if i >= 5:
                dp[i] = min(dp[i], dp[i - 5] + 1)

        return dp[amount]

    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
        """
        Top Down Memoization Approach using DFS. Similar to Target Sum.

        See simplified solution without memoization at coinChangeTopDownNoMemo
        """
        # Initialize size of memo array, we add 1 to amount to account for base case dp[0]=0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            # We are storing index=TOTAL to dp[i]=NUMBER_OF_COINS
            # We are storing the number of coins. So when we add a penny, that's one more coin!
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[amount] != float('inf'):
            return dp[amount]
        return -1

    def coinChangeDfs_TLE(self, coins: List[int], amount: int) -> int:
        """
        DFS approach - TLE, there isn't a way to use memo array.

        The other option when using DFS is to start at amount and work backwards.
        """
        # Try all possible combination of coins and constrain when the summation passes the given amount.
        # Every recursive call should add to the count
        def dfs(current, count):
            # Constraint - exceeded amount
            if current > amount:
                return

            # Amount reached
            if current == amount:
                result.append(count)
                return

            # Traverse neighbors
            for coin in coins:
                dfs(current + coin, count + 1)
            return

        result = []
        current = count = 0
        dfs(current, count)

        return min(result)

if __name__ == '__main__':
    print(Solution().coinChange(coins=[1,2,5], amount=100))
    # print(Solution().coinChangeGivenCoins(amount=100))