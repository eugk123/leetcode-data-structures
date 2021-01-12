"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Examples:
    Input:                                          Output:
(1) strs = ["eat","tea","tan","ate","nat","bat"]    [["bat"],["nat","tan"],["ate","eat","tea"]]
(2) strs = [""]                                     [[""]]
(3) strs = ["a"]                                    [["a"]]

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lower-case English letters.
"""
import collections
class Solution:
    def groupAnagrams(self, strs):  # HashMap [tuple] -> List
        """
        Intuition: Two strings are anagrams if and only if their sorted strings are equal.

        Algorithm: Maintain a map ans : {Tuple(String) -> List} where each key K is a sorted string, and each value is the
        list of strings from the initial input that when sorted, are equal to K.
        In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

        Time: O(N KlogK), where N is the length of strs, and K is the maximum length of a string in strs.
        The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
        Space: O(NK), the total information content stored in ans.

        Why do the keys need to be tuples in the python implementations?
        The key must be a tuple because tuples are immutable but a list is mutable. A dictionary key must be immutable.
        """
        ans = collections.defaultdict(list)     # This is dict[tuple] = list
        for s in strs:
            sorted_tuple = tuple(sorted(s))  # Sorting the tuple to create unique key entry into dictionary. Why tuple? See above.
            ans[sorted_tuple].append(s)  # For each matching unique tuple, we append string to the existing list.
        return ans.values()  # Returning only the values (collection of lists) of the dictionary.

    def groupAnagramsOptimized(self, strs):
        """
        Instead of using sorted tuples as the dict key, you can use character count.

        This is more optimize since there is no need to sort.

        Time is O(NK)
        """
        ans = dict()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if ans.get(tuple(count)) is None:
                ans[tuple(count)] = []
            ans[tuple(count)].append(s)  # Add the char tuple
        return ans.values()
if __name__ == '__main__':
    print(Solution().groupAnagramsOptimized(["bad", "adb", "pee", "eep"]))
