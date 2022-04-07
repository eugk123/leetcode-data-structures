"""
https://leetcode.com/problems/maximum-performance-of-a-team/
"""
from typing import List
import heapq
class Solution:
    """
    Sorting & Heap

    Sort all inputs based on efficiency in reverse (highest first). This is because we will mantain
    
    Input
    s=[10,7,6,3,2] 
    e=[3,2,5,1,6]
    k = 2

    Sort by efficiency in reverse
    s=[2,6,10,7,3]
    e=[6,5,3,2,1]

    Iterate through inputs, maintain a min heap sorted by speed
    - add (speed[i], efficiency[i]) to heap
    - maintain sum of speed, speed_sum
    - if len(heap) > k, subtract speed_sum by heapq.heappop(min_heap)[0]
    - add current speed[i] to speed_sum 
    - calculate performance and maintain max for result.
    """
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers
        # performance = sum(speed) * min(efficiency)
        sort_inputs = []
        for i in range(n):
            sort_inputs.append((efficiency[i], speed[i]))

        # Sort and update inputs
        sort_inputs.sort(reverse=True)
        min_heap_speed = []
        result = 0
        speed_sum = 0
        for i in range(n):
            efficiency[i], speed[i] = sort_inputs[i]
            
            # add everything to a heap sorted by speed (speed, efficiency)
            heapq.heappush(min_heap_speed, (speed[i], efficiency[i]))
            
            # speed sum decreases when heap size exceeds k
            if len(min_heap_speed) > k:
                speed_sum = speed_sum - heapq.heappop(min_heap_speed)[0] 

            # sum up next speed
            speed_sum = speed_sum + speed[i]

            # calculate max
            result = max(result, speed_sum * efficiency[i])

        return result % (10**9 + 7)
        
    def maxPerformanceSimple(self, n: int, speed: List[int], efficiency: List[int]) -> int:
        """
        Simple version, find max performance of entire team without k
        s=[10,7,6,3,2], e=[3,2,5,1,6]
        
        Sort by e
        s=[3,7,10,6,2]
        e=[1,2,3,5,6]
        """
        # performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers
        # performance = sum(speed) * min(efficiency)
        sort_inputs = []
        for i in range(n):
            sort_inputs.append((efficiency[i], speed[i]))

        # Sort and update inputs
        sort_inputs.sort()
        for i in range(n):
            efficiency[i], speed[i] = sort_inputs[i]
     
        # Get total speed, that way you can linearly sum up speeds when calculating performance
        total_speed = 0
        for current_speed in speed:
            total_speed = total_speed + current_speed
        
        # Get performance at every index. It is already optimized since efficiency is ordered.
        performance = []
        performance.append(total_speed * efficiency[0])
        for i in range(1, n):
            total_speed = total_speed - speed[i-1]
            performance.append(total_speed * efficiency[i])

        return max(performance)

if __name__ == '__main__':

    max_performance_simple = Solution().maxPerformanceSimple(5, [10,7,6,3,2], [3,2,5,1,6])
    print(max_performance_simple)