"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
from typing import List
import heapq
class Solution:
    """
    https://www.youtube.com/watch?v=cupg2TGIkyM

    Max Heap - Priority Queue
    O(N log k) time
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Get all frequencies for input strings
        map = dict()
        for word in words:
            if map.get(word) is None:
                map[word] = 1
            else:
                map[word] += 1

        # Put all the frequency pairings in a priority queue
        heap = [(-value, key) for key,value in map.items()]

        heapq.heapify(heap)

        # Grab the most frequent k words (stored on index [1]) using heappop
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

if __name__ == '__main__':
    print(Solution().topKFrequent(words=['ab','ab','abc','abcd','abcd'], k=2))