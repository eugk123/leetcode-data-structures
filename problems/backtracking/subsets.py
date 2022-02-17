"""
https://leetcode.com/problems/subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


"""
from typing import List
class Solution():
    def subsets(self, nums):
        """
        Backtracking solution as a directed graph visual.

        This is a directed graph problem. We traverse neighbors using array indices to the right of current node

        Subset time complexity is 2^n

        Total time and space complexity is O(2^n)
        """
        subsets = []

        def backtracking(index, subset):

            # End constraint
            if index == len(nums):
                subsets.append(subset)
                return

            subsets.append(subset)
    
            for i in range(index, len(nums)):
                backtracking(i + 1, subset + [nums[i]])
        
        backtracking(0, [])
        return subsets

    def subsetsBacktracking2(self, nums):
        """
        Backtracking
        https://www.youtube.com/watch?v=REOH22Xwdkk

                            []          1
                    /              \
                [1]                  []      2
                /       \           /       \
            [1,2]     [1]        [2]       []      4
            /    \    /   \      /   \     /  \
        [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3]  []     8 combinations

        There are N Strings in our array So there are N levels for RecursionTree and every Level has 2 options whether to include this String in our ans or not. That is why at the end we have
        2^N Combinations. Always think in terms of Levels and options.
        """
        def backtracking(index, subset):
            # Simply adding all leaf nodes which occurs when index == length of array
            if index == len(nums):
                subsets.append(subset)
                return

            # Add left node that adds next number to subset
            backtracking(index + 1, subset + [nums[index]])

            # Add right node that keeps existing subset
            # No need to worry about popping or backtracking here because we are not referencing the current subset
            backtracking(index + 1, subset)
        
        subsets = []
        backtracking(0, [])
        return subsets

    def subsetsBacktrackingMutable(self, nums):
        def backtracking(index):
            if index == len(nums):
                # We use list/copy to create new reference
                # If we don't create a new reference, it will append the subset of the final recursive run == []
                # The final run is the bottom right of the tree
                subsets.append(list(subset))  
                return

            subset.append(nums[index])
            backtracking(index + 1)
            subset.pop()  # Notice we have to pop since list object is mutable and being called outside
            backtracking(index + 1)

        subsets = []
        subset = []        
        backtracking(0)
        return subsets


if __name__ == '__main__':
    print(Solution().subsetsDfs([1,2,3]))

    # ['((()))', '(()())', '(())()', '()(())', '()()()']