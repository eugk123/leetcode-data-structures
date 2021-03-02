"""
https://leetcode.com/problems/climbing-stairs/
"""
class Solution:
    """
    Bottom-up Memoization
    https://www.youtube.com/watch?v=pQldnua_hZ4&list=PLujIAthk_iiO7r03Rl4pUnjFpdHjdjDwy&index=2&t=161s
    """
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)  # Initialize list based on length n
        memo[0] = 1  # Base Case
        memo[1] = 1  # Base Case
        return self.recurse(n, memo)

    def recurse(self, n, memo):
        # Check if current stairs value has already been computed - This speeds up computation time
        if memo[n] > 0:
            return memo[n]

        # Store current stairs value
        waysToCurrentStair = self.recurse(n - 1, memo) + self.recurse(n - 2, memo)
        memo[n] = waysToCurrentStair

        # Return current stairs value
        return waysToCurrentStair

if __name__ == '__main__':
    print(Solution().climbStairs(5))