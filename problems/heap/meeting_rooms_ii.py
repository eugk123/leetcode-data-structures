"""
https://leetcode.com/problems/meeting-rooms-ii/
"""
from typing import List
import heapq
class Solution:
    """
    https://jamboard.google.com/d/1phqgPD5Muf31ncfKkhbru-fSQNS2xTvlzedPEJTeAAI/viewer?f=0
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        occupied_rooms = []

        # Add first end time to min heap
        heapq.heappush(occupied_rooms, intervals[0][1])

        # Sort intervals 0th index ascending
        intervals.sort()

        # Iterate through intervals
        for i in intervals[1:]:
            # Check if min heap's end time is less than or equal to current interval's start time
            if occupied_rooms[0] <= i[0]:
                heapq.heappop(occupied_rooms)

            # Add current interval's end time to queue
            heapq.heappush(occupied_rooms, i[1])

        return len(occupied_rooms)

if __name__ == '__main__':
    print(Solution().minMeetingRooms(intervals=[[0,2],[1,7],[2,3],[3,6],[4,6],[5,8]]))
