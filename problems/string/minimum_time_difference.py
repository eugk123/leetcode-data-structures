"""
https://leetcode.com/problems/minimum-time-difference/submissions/
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        def convertToMins(time):
            hours = int(time[0:2])
            minutes = int(time[3:5])
            return hours * 60 + minutes

        # Pretty much you can take the difference of times forward and backwards. So you need to know the max minutes.
        max_minutes = 24 * 60

        prev_minutes = convertToMins(timePoints[len(timePoints) - 1])
        res = math.inf
        for time in timePoints:
            # Convert difference in time to total minutes
            minutes = convertToMins(time)
            print(prev_minutes, minutes)

            difference = abs(minutes - prev_minutes)
            # Take the min time between two points
            # We do min(minutes, max_minutes - minutes) to allow for the two time differences forward and backward
            # For example, we have between 00:00 and 10:00 -> we get min(10, 24-10) = 10
            res = min(difference, max_minutes - difference, res)

            # Update previous
            prev_minutes = minutes

        return res