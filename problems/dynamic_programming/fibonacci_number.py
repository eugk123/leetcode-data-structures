"""
https://leetcode.com/problems/fibonacci-number
"""
class Solution:
    def fib(self, n: int) -> int:
        def dfs(index):
            # MEMO Get
            if index in memo:
                return memo.get(index)
            
            # base cases
            if index == 0:
                return 0
            if index == 1:
                return 1

            # MEMO Update            
            memo[index] = dfs(index - 1) + dfs(index - 2)

            # recursive relationship fib(n) = fib(n-1) + fib(n-2)
            return dfs(index - 1) + dfs(index - 2)

        # MEMO Init
        memo = {}
        return dfs(n)

    def fibTLE(self, n: int) -> int:
        def dfs(index):
            # base cases
            if index == 0:
                return 0
            if index == 1:
                return 1
            
            # recursive relationship fib(n) = fib(n-1) + fib(n-2)
            return dfs(index - 1) + dfs(index - 2)

        return dfs(n)