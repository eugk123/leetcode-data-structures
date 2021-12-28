"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
"""
from typing import List
class Solution():
    def maxLengthDfs(self, arr):
        """
        DFS solution - traverse neighbors located right of current index

        https://www.youtube.com/watch?v=pKYmv4Hdao4&t=1109s

        Subset overall complexity = 2^n
        With list to set conversion -> time complexity of n
        
        Time complexity = O(n * 2^n)
        Space complexity = O(2^n)
        """
        def hasDuplicates(subset_string):
            # Check if duplicate character
            # Use a set on a char array of current word
            if len(subset_string) == len(set(subset_string)):
                return False
            return True
        
        def dfs(index, subset_string):
            
            if len(subset_string) == len(set(subset_string)):                
                # Update max length
                self.result = max(self.result, len(subset_string))
            
            # Traverse neighbors (only nodes right of current index)
            for i in range(index, len(arr)):
                # Check if it has duplicate characters, if not, then continue
                if not hasDuplicates(subset_string + arr[i]):
                    dfs(i + 1, subset_string + arr[i])
        
        
        self.result = 0
        dfs(0, "")
        
        return self.result

    def maxLengthBacktracking(self, arr):
        """
        Backtracking solution for subsets:

                            []                     -start empty1  ->  1 combination
                    /              \
                [un]                  []         -index 1 ("un") or empty  ->  2 combinations
                /       \           /       \
            [uniq]     [un]     [iq]       []     -index 2 ("iq") or empty  ->  4 combinations
            /    \    /   \      /   \     /  \
        [unique]     [unue]    [ique] [iq] [ue] []  -index 3 ("ue") or empty  ->  8 combinations
                [uniq]      [un]

        Time complexity results in O(2^n) since we're sending two search parties at every index
        """
        def hasDuplicates(subset_string):
            # Check if duplicate character
            # Use a set on a char array of current word
            if len(subset_string) == len(set(subset_string)):
                return False
            return True
            
        def backtracking(index, subset_string):
            # End at passing final index
            if index == len(arr):
                # Update max length
                self.result = max(self.result, len(subset_string))
                return
            
            # Update max length
            self.result = max(self.result, len(subset_string))
            
            # Decision to traverse with addition of next string
            if not hasDuplicates(subset_string + arr[index]):
                backtracking(index + 1, subset_string + arr[index])

            # Decision to traverse keeping current string
            if not hasDuplicates(subset_string):
                backtracking(index + 1, subset_string)

        
        self.result = 0
        backtracking(0, "")
        
        return self.result



if __name__ == '__main__':
    print(Solution().maxLengthDfs(["ue", "ui", "iq"]))