"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""
class Solution:
    """
    Top Down DFS

    Maximize Sum while exploring all possible paths. Similar to House Robber.
    startTime = [ 1, 2, 3, 3]
    endTime   = [ 3, 4, 5, 6]
    profit    = [50,10,40,70]
    1->3 = 50, 3->5 = 40... 1->5 = 90
    1->3 = 50, 3->6 = 70... 1->6 = 120

    Notice that we can add profits to previous paths where the startTime (current) >= endTime (previous)
    1->3  prevEndTime = 3
    3->5 and 3->6  currentStartTime = 3
    > profit[index] + dfs(endTime converted to startTime index)
    This "endTime converted to startTime index" how do we get this? We can get this using binary search since the array is sorted!

    We also want to explore all paths to the right:
    > dfs(index + 1) 

    Unique to this problem:
    - Input can be unsorted. We need to sort all inputs based on startTime. -> O(N)
    - When exploring the summation path, make sure to perform binary search to find the next start index.

    https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/918804/Python-Top-Down-and-Bottom-Up-DP-7-lines-each
    """
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def binary_search(i):
            end = endTime[i]
            
            # if end time exceeds max start time, we can return the end so we ignore this path
            if end > max_start_time:
                return len(startTime)
                
            # perform binary search to look for the index where end time matches start time.
            left, right = 0, len(startTime)
            while left <= right:
                # calculate mid
                mid = left + (right - left)//2

                # The end index is found when the end value is between adjacent start values
                # ex: startTime = [1,2,4,6] endTime = [3,5,6,7]
                # For index = 0, start = startTime[0] = 1, end = endTime[0] = 3
                # Since end falls between 2 and 4 and index 1 and 2 respectively,
                # We update start_to_end_index[start_index -> 0] = end_index -> 2
                if mid > 0:
                    if startTime[mid - 1] < end <= startTime[mid]:
                        return mid
                        
                # update left to mid
                if startTime[mid] < end:
                    left = mid + 1

                # update right to mid
                else:
                    right = mid - 1
            return len(startTime)


        # sort by startTime
        sort_inputs = []        
        for i in range(len(startTime)):
            sort_inputs.append((startTime[i], endTime[i], profit[i]))
        sort_inputs.sort()
        
        # reset inputs now that they are sorted
        startTime, endTime, profit = [], [], []
        for start, end, cprofit in sort_inputs:
            startTime.append(start)
            endTime.append(end)
            profit.append(cprofit)
        
        # perform binary search to find next start times that follow from previous end time.
        # that's how we reach the next path when we add the profit for the previous start time.
        start_to_end_index = {}
        max_start_time = max(startTime)
        for i in range(len(startTime)):
            start = startTime[i]
            end = endTime[i]
            
            # if end time exceeds max start time, we can skip this
            if end > max_start_time:
                start_to_end_index[i] = len(startTime)
                continue
                
            # perform binary search to look for the index where end time matches start time.
            left, right = 0, len(startTime)
            while left <= right:
                # calculate mid
                mid = left + (right - left)//2

                # The end index is found when the end value is between adjacent start values
                # ex: startTime = [1,2,4,6] endTime = [3,5,6,7]
                # For index = 0, start = startTime[0] = 1, end = endTime[0] = 3
                # Since end falls between 2 and 4 and index 1 and 2 respectively,
                # We update start_to_end_index[start_index -> 0] = end_index -> 2
                if mid > 0:
                    if startTime[mid - 1] < end <= startTime[mid]:
                        start_to_end_index[i] = mid
                        break
                        
                # update left to mid
                if startTime[mid] < end:
                    left = mid + 1

                # update right to mid
                else:
                    right = mid - 1
        print(startTime)
        print(endTime)
        
        # top down dfs
        def dfs(index):
            # out of bounds, return 0
            if index == len(startTime): 
                return 0
            
            if index in memo:
                return memo.get(index)

            # try all possible paths
            a = dfs(index + 1)
            
            # take sum and the next index will be the next start time using previous end time
            end_index = start_to_end_index[index]
            b = profit[index] + dfs(end_index)
            
            memo[index] = max(a, b)
            return max(a, b)
        
        memo = {}
        return dfs(0)

    def jobSchedulingTLE(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by startTime
        sorted_start_end = []        
        for i in range(len(startTime)):
            sorted_start_end.append((startTime[i], endTime[i], profit[i]))
        sorted_start_end.sort()
        print(sorted_start_end)
        
        # top down dfs
        def dfs(index, current_end_time, current_profit):
            print(index, current_profit) 
            
            # optimize for max profit
            if current_end_time > last_start_time:
                return current_profit
            
            ans = 0            
            for i in range(len(sorted_start_end)):
                
                # try all subsequent start times greater than current time = previous end time
                if current_end_time <= sorted_start_end[i][0]:                    
                    ans = max(ans, dfs(i, sorted_start_end[i][1], current_profit + sorted_start_end[i][2]))
                    
            return ans
        
        last_start_time = max(startTime)
        return dfs(0, 0, 0)