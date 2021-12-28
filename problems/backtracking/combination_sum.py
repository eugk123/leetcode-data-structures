"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
from typing import List
class Solution:
    """
    Backtracking - get all possible combinations until target is reached. no limit on level/index.
    ex: candidates = [2,3,5]
    level
    0       []
    1       [2]             [3]         [5]
    2       [22][23][25]    [33][35]    [55]
    3*      [222][223][225] [333][335]  [555]
    4*      [2222][2223][2225]
    
    level 3 and 4 branches only show from leftmost combination ([2,2], [3,3], [5,5])

    Where n = len(candidates) and m = target/(avg candidate)
    Time complexity: O(n^m)
    The height of the tree would be target and degree of each node would be number of candidates. 

    Space complexity: O(m)??
    
    More on complexity - https://leetcode.com/problems/combination-sum/discuss/742449/Explanation-of-Time-Complexity/1145094/
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        candidates.sort()
       
        def dfs(index, combination, total):
            # Total goes beyond target, end
            if total > target:
                return
           
            # Current total equals target, end and append to result
            if total == target:
                result.append(combination)
                return
           
            # We iterate through every possible index to the right inclusive of current index.
            # As index increases, the range should decrease. 
            for i in range(index, len(candidates)):
                dfs(i, combination + [candidates[i]], total + candidates[i])
       
        result = []
        dfs(0, [], 0)
        return result

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))