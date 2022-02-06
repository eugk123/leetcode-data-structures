"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/
"""
class Solution(object):
    """
    Use two pointer prev and curr interval.

    While the prev end is greater than the curr beginning, 
        Traverse curr pointer until this condition is met. 
        Count this once as one arrow. 
    Then update prev to curr.

    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    try left to right - 
    arrow shoots through under these conditions
    (1) when prev end >= curr beg
    (2) when minimum end >= curr beg
    0123456789012 
    ---------- p min end = 10
    ------- c update min end = 9
        -------- c
        -- c update min end = 7
        ---- c
            ----- p c couldn't satisfy shoot conditions, update prev and set min end back to prev end
            ---- c
    """
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        print(points)
        
        # left to right
        prev = points[0]
        min_end = prev[1]
        result = 1
        for i in range(1, len(points)):
            curr = points[i]
            
            # keep traversing current until beginning of current > end of previous
            if prev[1] >= curr[0] and curr[0] <= min_end:
                min_end = min(min_end, curr[1])  # update minimum end because it may be further left and next interval be further right meaning it cannot be hit by same arrow
                continue

            result += 1                
            prev = curr
            min_end = prev[1] # update minimum end to prev end
        
        return result
