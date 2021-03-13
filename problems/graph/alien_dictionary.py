"""
https://leetcode.com/problems/alien-dictionary/
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        https://www.youtube.com/watch?v=fhCXVABhFDc
        """
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = {}
        in_degree = [0] * 26

        for word in words:
            for letter in word:
                if letter not in adj_list:
                    adj_list[letter] = set()

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            min_length = min(len(first), len(second))

            # Compare letter by letter using the min length
            for j in range(min_length):
                if first[j] != second[j]:
                    if second[j] not in adj_list.get(first[j]):
                        adj_list[first[j]].add(second[j])
                        in_degree[ord(second[j]) - ord('a')] += 1
                    break

            # Check that second word isn't a prefix of first word.
            else:
                if len(second) < len(first): return ""

        # Step 2: We need to repeatedly pick off nodes with an in_degree of 0.
        res = []
        queue = deque([])

        # Add all in_degree 0s to queue
        for letter in adj_list:
            if in_degree[ord(letter) - ord('a')] == 0:
                queue.append(letter)

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nei in adj_list[curr]:
                in_degree[ord(nei) - ord('a')] -= 1
                if in_degree[ord(nei) - ord('a')] == 0:
                    queue.append(nei)

        # If not all letters are in result, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(res) < len(adj_list):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(res)