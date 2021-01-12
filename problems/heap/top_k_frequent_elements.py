"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
from typing import List
import heapq
class Solution:
    """
    Priority Queue for Max Heap
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a map of num to frequency - O(n) time
        map = dict()
        for num in nums:
            if map.get(num) is None:
                map[num] = 1
            else:
                map[num] += 1

        # Rearrange dictionary into list of tuples
        max_heap = [(-value, key) for key, value in map.items()]

        # Heapify
        heapq.heapify(max_heap)

        # Heappop taking the front element. Take the number using index [1].
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res

if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[5,8,8,8,6,6,9,10], k=2))