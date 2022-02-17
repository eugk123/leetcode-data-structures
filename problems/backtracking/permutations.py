"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution():
    def permuteVisited(self, nums):
        """
        Backtracking w/ decision space/visited array
        
                path                                                    visited array
        level0: []                                                      [1,2,3]
        level1: [1]                  [2]              [3]               [2,3]       [1,3]       [1,2]
        level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]       [3]         [2]         [1]
        level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]    []          []          []

        Assuming n = length of nums,
        Time complexity: O(n * n!) 
        Based on permutation backtracking resulting in n! due to reduced decision tree per level and set conversion of linear time 
        Space complexity: O(n * n!) 
        Based on total number of permutations equal to n! and deep copies of list due to current + [nums[i]] as an input in the dfs equation

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, visited, permutation):
            # We don't want duplicate permutations
            if permutation in result:
                return
            
            # Trying to catch distinct permutations, meaning the length of current permutation must equal length of input
            if len(permutation) == len(nums):
                result.append(permutation)
                return
            
            for i in range(len(nums)):
                # If next neighbor is visited, skip
                if nums[i] not in visited:
                    dfs(index + 1, visited + [nums[i]], permutation + [nums[i]])
                
        result = []
        dfs(0, [], [])
        return result

    def permuteSet(self, nums):
        """
        Backtracking - send search party at every index for a permutation is O(n!)

        Instead of using a visitor array, you can use a set() condition to ignore duplicates.

        This makes code even cleaner.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(current):
            # Trying to catch distinct permutations, meaning the length of current set must equal length of input
            if len(current) == len(nums):
                result.append(current)
                        
            for i in range(len(nums)):
                # skip duplicate numbers
                if len(set(current + [nums[i]])) == len(current + [nums[i]]):
                    dfs(current + [nums[i]])
                    
        result = []
        dfs([])
        return result
if __name__ == '__main__':
    print(Solution().permuteVisited([1,2,3]))
