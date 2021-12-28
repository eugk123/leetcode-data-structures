"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution():
    def permuteWithDups(self, nums):
        """
        Backtracking - send search party at every index for a permutation is O(n!)

        This solution is very similar to Permutation I using a visitor array. But with one caveat. The visitor array containing nums values will not work
        due to duplicate elements. To handle duplicates, you need to use the indices instead since that will always be unique.
        Therefore, a visited_indices is the way to go here.
        
        Another caveat is when performing DFS, you will notice duplicates. We can do a simple lookup on the resultant list to ignore duplicate permutations.  

        Assuming n = length of nums,
        Time complexity: O(n * n!) 
        Based on permutation backtracking resulting in n! due to reduced decision tree per level and set conversion of linear time 
        Space complexity: O(n * n!) 
        Based on total number of permutations equal to n! and deep copies of list due to current + [nums[i]] as an input in the dfs equation

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, visited_indices, permutation):
            # We don't want duplicate permutations
            if permutation in result:
                return
            
            # Trying to catch distinct permutations, meaning the length of current permutation must equal length of input
            if len(permutation) == len(nums):
                result.append(permutation)
                return
            
            for i in range(len(nums)):
                # Cannot add it's current index. Skip that one.
                if i not in visited_indices:
                    dfs(index + 1, visited_indices + [i], permutation + [nums[i]])
                    
        result = []
        dfs(0, [], [])
        return result

if __name__ == '__main__':
    print(Solution().permuteWithDups([1,2,3]))

    # ['((()))', '(()())', '(())()', '()(())', '()()()']