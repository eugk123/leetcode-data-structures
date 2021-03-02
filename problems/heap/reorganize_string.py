"""
https://leetcode.com/problems/reorganize-string/
"""
import heapq
import collections
class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Greedy Algorithm
        https://www.youtube.com/watch?v=zaM_GLLvysw
        https://leetcode.com/problems/reorganize-string/discuss/130825/Python-solution-with-detailed-explanation
        """
        # Initialize frequency map
        map = dict()
        for char in s:
            if map.get(char) is None:
                map[char] = 1
            else:
                map[char] += 1

        # Find max frequency. Determine if there are enough characters to fit between the gaps.
        # You'll notice that the min length is 2*max_freq - 1. So if max_freq is greater, return ""
        max_freq = 0
        for i in map:
            max_freq = max(max_freq, map.get(i))

        if 2 * max_freq - 1 > len(s):
            return ""

        # Rearrange dictionary into list of tuples then heapify.
        max_heap = [(-value, key) for key, value in map.items()]
        heapq.heapify(max_heap)
        print(max_heap)

        ans = []
        # Grab letter from front + 1 index. Reduce frequency by 1. If only 1, remove
        while len(max_heap) >= 2:
            nct1, ch1 = heapq.heappop(max_heap)
            nct2, ch2 = heapq.heappop(max_heap)

            ans.extend([ch1, ch2])
            if nct1 + 1 != 0:
                heapq.heappush(max_heap, (nct1 + 1, ch1))
            if nct2 + 1 != 0:
                heapq.heappush(max_heap, (nct2 + 1, ch2))

        if max_heap:
            final_char = max_heap[0][1]
        else:
            final_char = ''

        return ''.join(ans) + final_char


if __name__ == '__main__':
    print(Solution().reorganizeString(s='aab'))