"""
https://leetcode.com/problems/climbing-stairs/
"""
class Solution:
    """
    Top-down Memo 1D

    Counting total number of possibilities. 
    - Out of bounds return: 0
    - End of array return: 1
    - End return: summation of paths (a + b)

    Time O(N)
    """
    def climbStairs(self, n: int) -> int:
        def dfs(index):
            # MEMO Get
            if index in memo:
                return memo[index]

            # out of bounds, don't count
            if index > n:
                return 0

            # end is reached, count
            if index == n:
                return 1
            
            a = dfs(index + 1)
            b = dfs(index + 2)

            # MEMO Update
            memo[index] = a + b
            
            return a + b
        # MEMO Init
        memo = {}
        return dfs(0)

    def climbStairsTLE(self, n: int) -> int:
        def dfs(index):

            # out of bounds, don't count
            if index > n:
                return 0
                
            # end is reached, count
            if index == n:
                return 1
            
            a = dfs(index + 1)
            b = dfs(index + 2)
            
            return a + b
        return dfs(0)
if __name__ == '__main__':
    print(Solution().climbStairs(5))