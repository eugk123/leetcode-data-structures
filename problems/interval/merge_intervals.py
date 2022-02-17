"""
https://leetcode.com/problems/merge-intervals/
"""
from typing import List
class Solution:
    """
    Sorting

    Time O(nlogn)
    Space O(n)
    """
    def mergeEugene(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            prev = result.pop()
            curr = intervals[i]
            
            if prev[1] < curr[0]:
                result.append(prev)
                result.append(curr)
            elif prev[1] >= curr[0] and prev[1] < curr[1]:
                result.append([prev[0],curr[1]])
            elif prev[1] >= curr[0] and prev[1] >= curr[1]:
                result.append([prev[0],prev[1]])
            else:
                result.append(prev)
        return result
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Base Case - len = 1
        if len(intervals) == 1:
            return intervals

        # First sort the array in ascending order. Sort command will sort based on first index of interval.
        intervals.sort()

        # If the last index of previous interval <= first index of current interval,
        # then update the first index of current interval with first index of previous interval
        # otherwise continue.
        pop_indices = []
        for i in range(len(intervals)):
            # If last index of current is less (this should consume the whole interval)
            if i > 0 and intervals[i-1][1] >= intervals[i][1]:
                intervals[i] = intervals[i - 1]
                pop_indices.append(i-1)

            # If last index of current is greater
            elif i > 0 and intervals[i-1][1] >= intervals[i][0]:
                intervals[i] = [intervals[i-1][0], intervals[i][1]]
                pop_indices.append(i-1)

        for index in reversed(pop_indices):
            intervals.pop(index)
        return intervals


if __name__ == '__main__':
    print(Solution().merge(intervals=[[2,6],[8,10],[1,15],[15,18]]))
