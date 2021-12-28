"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
from typing import List
class Solution:
    """
    Backtracking - solution similar to Combination Sum I, with the following changes:
    1) an additional condition to not send search party on duplicates
    2) when sending search parties, traverse an additional index because we want only distinct numbers

    Leetcode solution is free: https://leetcode.com/problems/combination-sum-ii/solution/
    Time complexity: O(2^n)
    The result is similar to subsets in the sense where we have distinct numbers in each combination.
    Ignore the target and draw out all possible subsets.

    candidates = [1 2 3]
    4       2       1
    [1]     [2]     [3]
    [12][13][23]
    [123]

    candidates = [1 2 3 4]
    8               4           2       1
    [1]             [2]         [3]     [4]
    [12][13]  [14]  [23][24]    [34]    
    [123][124][134] [234]
    [1234]

    Space complexity: O(n)
    We apply recursion in the algorithm, which will incur additional memory consumption in the function call stack. 
    In the worst case, the stack will pile up to O(N) space.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        candidates.sort()
       
        def dfs(index, combination, total):
            if total > target:
                return
           
            if total == target:
                result.append(combination)
                return
           
            for i in range(index, len(candidates)):
                # Duplicate tree when the next number has the same value
                if candidates[i] == candidates[i - 1] and i > index:
                    continue   

                # index = i + 1 because we do not want to include the current candidate
                dfs(i + 1, combination + [candidates[i]], total + candidates[i])
       
        result = []
        dfs(0, [], 0)
        
if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5],8))