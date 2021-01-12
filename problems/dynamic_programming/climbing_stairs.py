"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
class Solution:
    """
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