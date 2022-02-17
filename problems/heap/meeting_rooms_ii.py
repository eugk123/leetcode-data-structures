"""
https://leetcode.com/problems/meeting-rooms-ii/
"""
from typing import List
import heapq
class Solution:
    """
    https://jamboard.google.com/d/1phqgPD5Muf31ncfKkhbru-fSQNS2xTvlzedPEJTeAAI/viewer?f=0
    """
    def minMeetingRoomsEugene(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        min_heap = []
        result = 0
        
        for interval in intervals:
            
            # if min heap ending time is before the start time of current interval, pop it.
            if min_heap:
                # heap[0] is the min heap
                # we use heapq.heappop(min_heap), to pop the minimum number
                if min_heap[0] <= interval[0]:
                    heapq.heappop(min_heap)

            # Add current interval ending time to heap
            heapq.heappush(min_heap, interval[1])  # push the end of each interval

            # we use a min heap containing all the end times of each interval coming in.
            # the size of the heap will be the result
            result = max(len(min_heap), result)
            
        return result
        
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
