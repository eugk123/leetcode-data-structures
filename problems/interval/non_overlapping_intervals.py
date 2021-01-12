"""
https://leetcode.com/problems/non-overlapping-intervals/
"""
from typing import List
class Solution:
    """
    Sort then check for overlaps between current and previous.
    """

    class Solution:
        def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

            # First sort the intervals:
            intervals.sort()

            res = 0
            for i in range(len(intervals)):
                if i > 0:

                    # Notice that current and previous intervals overlap using the last index of previous and first index of current.
                    if intervals[i - 1][1] > intervals[i][0]:

                        res += 1  # Add count

                        # Scenario 1: Full overlap (prev overlaps curr) - Take curr since smaller
                        if intervals[i - 1][1] >= intervals[i][1]:
                            # keep and move on
                            continue

                        # Scenario 1: Partial overlap - Take previous interval
                        else:
                            intervals[i] = intervals[i - 1]  # replace with previous
                            continue
            return res


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals(intervals=[[1,3],[2,30],[5,7],[7,10],[11,12]]))
