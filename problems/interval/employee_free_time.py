"""
https://leetcode.com/problems/employee-free-time
"""
# Definition for an Interval. GIVEN
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    """
    input
    - schedule is a array of employee working time
    - non overlapping intervals
    - interval class is employee working time

    return free_schedule [[Interval]]
    - common, + free time for all employees
    - sorted

    [
    [[1,2],[5,6]],  employee_schedule1
    [[1,3],[4,10]]  employee_schedule2
    ]

    []  []
    [ ][     ]->[ ][     ]  which leaves with [3,4] being the only available free time
    1234567890  1234567890

    collect all intervals, then sort:
    [[1, 2], [1, 3], [4, 10], [5, 6]]

    merge intervals
    [[1, 3], [4, 10]]]

    add remaining gaps to empty result array
    result = [3,4]


    example merge conditions
    1       2         3               
    ----    --------  -----    
    ----   ----       ------   
    ----    --------  ---------
    ----   skip     [pl,cr]
                    update pr with cr
    update
    pl & pr
    """    
    def employeeFreeTime(self, schedule) 
        # schedule: '[[Interval]]' -> '[Interval]'
                
        working_schedule = []
        for employee_schedule in schedule:
            for interval in employee_schedule:            
                working_schedule.append([interval.start, interval.end])
                
        working_schedule.sort()
        print(working_schedule)

        pl, pr = working_schedule[0][0], working_schedule[0][1]
        merge_intervals = [working_schedule[0]]
        for interval in working_schedule[1:]:
            cl, cr = interval[0], interval[1]
            
            # merge conditions
            # 1 - separated
            if pr < cl:
                merge_intervals.append(interval)
            # 3 - previous overlaps partially
            elif pl <= cl and pr >= cl and pr <= cr:
                merge_intervals.pop()
                merge_intervals.append([pl,cr])
                
                # update previous right
                pr = cr
                continue
            # 2 - previous overlaps completely 
            else:
                # don't update previous pointers
                continue

            # update previous left and right
            pl, pr = cl, cr
        print(merge_intervals)
        
        # now we need to populate the spaces into the results from merged intervals
        result = []
        prev = merge_intervals[0]
        for interval in merge_intervals[1:]:
            result.append(Interval(prev[1], interval[0]))
            prev = interval
            
        return result
