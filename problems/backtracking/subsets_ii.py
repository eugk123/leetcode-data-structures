"""
https://leetcode.com/problems/subsets-ii/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Time complexity: O(2^n * n) - 2^n for subset backtracking and n for checking duplicates
Space complexity: O(2^n * n) - 2^n for total number of subsets of size n and n for deep copies of subset from parameter input subset+[nums[i]]
"""
from typing import List
class Solution():
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # With duplicate numbers, there will always be duplicate subsets. Try drawing it out.
        # If the duplicate inputs are not sorted, then there will be subsets with different orders
        # e.g. [1,2] and [2,1] shouldn't both be in the result. So we need to sort the input.
        nums.sort()
        
        # Same backtracking equation used in subsets i with one additional check
        def backtracking(index, subset):
            # This is the additional check to check if there are duplicates
            if subset in result:
                return
            
            if index == len(nums):
                result.append(subset)
                return
            
            result.append(subset)
            
            for i in range(index, len(nums)):
                # notice that we don't include subset where (1) the current val same as previous val and (2) the current index "i" differs from the previous index "index".
                if i > 0:
                    if nums[i-1] == nums[i] and i != index:
                        continue
                backtracking(i + 1, subset + [nums[i]])    
        
        result = []
        backtracking(0, [])
        return result


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1,2,2]))