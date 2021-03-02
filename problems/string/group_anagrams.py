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
        # Base case - empty list
        if not strs:
            return strs

        # This map will contain value (counts of each ord(char)) to key (list of anagrams)
        map = {}

        # Iterate through each word. The idea is to have a unique key that matches all valid anagrams to group them in the map key.
        for word in strs:

            # Map key will contain a tuple of 26 values that contain the count of each letter.
            count = [0] * 26
            for letter in word:
                ord_val = ord(letter) - ord('a')
                count[ord_val] += 1

            # Convert count to tuple (key in map has to be immutable)
            count = tuple(count)

            # Create an entry in the map if it doens't exist
            if not map.get(count):
                map[count] = [word]
            else:
                map[count].append(word)

        # Iterate through each map key and append to result.
        res = []
        for key in map:
            res.append(map.get(key))

        return res
if __name__ == '__main__':
    print(Solution().groupAnagramsOptimized(["bad", "adb", "pee", "eep"]))
