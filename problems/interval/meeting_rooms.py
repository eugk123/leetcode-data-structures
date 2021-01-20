"""
https://leetcode.com/problems/meeting-rooms/
"""
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()  # Sort by first number ascending

        for i in range(len(intervals)):
            # Check if first interval overlaps with second interval
            if i > 0 and intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
if __name__ == '__main__':
    print(Solution().canAttendMeetings(intervals=[[0,15],[15,30]]))
