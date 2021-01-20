"""
https://leetcode.com/problems/meeting-scheduler/submissions/
"""
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Merge both slots and return only the differences
        intervals = slots1 + slots2
        intervals.sort()
        differences = []
        for i in range(len(intervals)):
            # Check overlap between previous and current index
            if i > 0:
                # If current start <= previous end AND current end > previous end
                if intervals[i][0] <= intervals[i - 1][1] and intervals[i][1] > intervals[i - 1][1]:
                    end = intervals[i - 1][1]
                    start = intervals[i][0]

                # If current start <= previous end AND current end <= previous end
                elif intervals[i][0] <= intervals[i - 1][1] and intervals[i][1] <= intervals[i - 1][1]:
                    end = intervals[i][1]
                    start = intervals[i][0]

                # If not overlapping, skip to next
                else:
                    continue

                differences.append([start, end])

        # Take the new slots and check if duration fits
        for start, end in differences:

            # If duration fits, then return first one plus duration.
            if end - start >= duration:
                return [start, start + duration]