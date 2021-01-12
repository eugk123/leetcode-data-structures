"""
https://leetcode.com/problems/insert-interval/
"""
from typing import List
class Solution:
    """
    Leverage Merge Interval solution.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Base Case - empty newInterval or intervals
        if newInterval == []:
            return intervals
        if intervals == []:
            return [newInterval]

        # Append newInterval
        for i in range(len(intervals)):
            # newInterval first index is same as currentInterval first index
            if intervals[i][0] == newInterval[0]:
                if intervals[i][1] < newInterval[1]:  # newInterval larger, so insert
                    intervals.insert(i, newInterval)
                    break
                else:  # newInterval fits within, so do nothing
                    break
            print(intervals[i][0], newInterval[0])
            # newInterval first index is less than currentInterval first index
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break

            # If we reached end, just append
            if i == len(intervals) - 1:
                intervals.append(newInterval)

        # (Taken from Merge Intervals, but no sorting)
        # If the last index of previous interval <= first index of current interval,
        # then update the first index of current interval with first index of previous interval
        # otherwise continue.
        pop_indices = []
        for i in range(len(intervals)):
            # If last index of current is less (this should consume the whole interval)
            if i > 0 and intervals[i - 1][1] >= intervals[i][1]:
                intervals[i] = intervals[i - 1]
                pop_indices.append(i - 1)

            # If last index of current is greater
            elif i > 0 and intervals[i - 1][1] >= intervals[i][0]:
                intervals[i] = [intervals[i - 1][0], intervals[i][1]]
                pop_indices.append(i - 1)

        for index in reversed(pop_indices):
            intervals.pop(index)
        return intervals


if __name__ == '__main__':
    print(Solution().merge(intervals=[[1,3],[6,9]],newInterval=[2,5]))
