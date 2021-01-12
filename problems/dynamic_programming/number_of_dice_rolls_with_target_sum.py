"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum
"""
class Solution:
    """
    https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
    """
    def numRollsToTarget(self, d: int, f: int, t: int) -> int:
        memo = {}
        def dp(dice, target):
            # Base case - Target bigger than f*dice. So if we have 6 dices with 6 faces, target cannot be greater than 36.
            if target > f*dice:
                memo[dice, target] = 0
                return 0

            # Base case - 0 dices -> return 0 (covered above)
            # if dice == 0 and target > 0:
            #     return 0

            # Base case - target and dice == 0 -> return 1
            # This is because when taking the smallest possible solution dp(1,1) = 1. When putting this into
            # the recursive equation: dp(n-1,t-1) = dp(0,0). Therefore, dp(0,0) must = 1.
            if dice == 0 and target == 0:
                return 1

            # Base Case - negative target -> return 0
            if target < 0:
                return 0


            # # Base case - Target is negative, return 0
            # if target < 0: return 0

            # Check memo
            if (dice, target) in memo:
                return memo[dice, target]

            # dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
            # We can replace f using a for loop going from (1, f)
            ways = 0
            for num in range(1, f+1):
                ways += dp(dice-1, target-num)
            memo[dice, target] = ways
            return ways
        return dp(d, t) % (10**9+7)

    def test(self, x, y):
        if x == 0:
            return y == 0

if __name__ == '__main__':
    print(Solution().numRollsToTarget(d=6,f=6,t=15))
