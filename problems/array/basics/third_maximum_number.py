"""
https://leetcode.com/problems/third-maximum-number/
"""
import heapq
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/third-maximum-number/discuss/90272/python-solution-with-detailed-explanation

        Use a set to remove duplicates.
        Use a max heap (PQ) via negative heapify and grab the 3rd maximum by popping 3 times.
        Building a heap (heapify) is O(n) time.
        """
        # Quick way is to sort descending then add to a set() to remove duplicates and grab the 3rd index.
        # But the problem wants an O(n) time solution.

        # Remove duplicates by passing elements into a set. Make the new list negative for your max heap.
        nums = set(nums)
        max_heap = []
        for num in nums:
            max_heap.append(-num)

        # Build heap - O(n).
        heapq.heapify(max_heap)

        # Pop 3 times for max. If less than 3 elements, then just pop once to get the max.
        count = 0
        if len(max_heap) >= 3:
            while count <= 2:
                max_number = heapq.heappop(max_heap)
                count += 1
        else:
            max_number = heapq.heappop(max_heap)

        # Return positive number.
        return -max_number

if __name__ == '__main__':
    print(Solution().thirdMax(nums=[-100,10,20,30]))
