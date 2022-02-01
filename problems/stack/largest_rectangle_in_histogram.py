"""
https://leetcode.com/problems/largest-rectangle-in-histogram
"""
class Solution:
    """
    At every index, you'll need to provide the minimum height that will be used to compute area across all indices.

    O(n^2) brute force solution:
    Brute force, we iterate over n times n^2 using the current value as the height
    2 1 5 6 2 3
    2 + 2 from [2 3] = 4
    1 from all = 6
    5 from [5 6] = 10
    6 from [6] = 6
    3 from [5 6] = 6
    result = 10

    O(n) solution using stack:
    This can be incredibly confusing. If you have an ascending histogram, it is very easy to calculate all possible areas since the minimum height for each value is at the leftmost index.
    
    We pretty much do the same exact thing, except we use a stack to keep track of the leftmost indices paired with the height (height, left). 
    
    At every iteration, 
        - When peek height > current height, we add to stack as (height, left) 
        - When equal, we compute and traverse next. 
        - When peek height < current height, we pop, then we enter a while loop that keep computing and popping until (1) stack is empty, or (2) peek height > current height again.
    At the end, we will likely have a stack with ascending heights and left indices. We compute areas and pop until stack is empty.
   . 
    The idea is that as you traverse from left to right, we want to maintain a stack containing the leftmost index for a par
    2 1 5 6 2 3     stack
    i               [(2,0)]
      i             [] -> [(1,0)],   peek 2 > curr 1, we keep the left index when we add to stack because we will be calculating the total area from index 0 for height 1
        i           [(1,0)],  peek 1 < curr 5, add to stack: [(1,0), (5,2)]
          i         [(1,0), (5,2)] peek 5 < curr 6, add to stack: [(1,0), (5,2), (6,3)]
            i       [(1,0), (5,2), (6,3)], 6 > 2, peek=6 left=3, pop until stack is empty or peek > curr, stack: [(1,0)] -> [(1,0),(2,4)]. See ** for more
              i     [(1,0), (2,2), (3,5)], now i = 5, we've reached the end, we know our stack will always be ascending heights, so we simply work backwards until all possible areas are calculated. See ***

    **
    i = 4, height[i] = 2
    [(1,0), (5,2), (6,3)]   (2,4) < (6,3) No. result = peek * (i - left) = 6 * (4-3) = 6,  previous_left = 3
    [(1,0), (5,2)]          (2,4) < (5,2) No. result = 5 * (4-2) = 10, previous_left = 2
    [(1,0)]                 (2,4) < (1,0) Yes, add to stack as (height, previous_left) = (2,2)

    ***
    i = 5
    [(1,0), (2,2), (3,5)]   (3,5) -> result = peek * (i - left + 1) = 3 * (5 - 5 + 1) = 3
    [(1,0), (2,2)]          (2,2) -> result = 2 * (5 - 2 + 1) = 8
    [(1,0)]                 (1,0) -> result = 1 * (5 - 0 + 1) = 6
    []                      empty. end.

    Now what about equal numbers peek == curr?
    2 2 2 2     stack
    i           [(2,0)]
      i         [(2,0)]  res = peek * (i - left + 1) = 2 * (1 - 0 + 1) = 4
        i       [(2,0)]  res = 2 * (2 - 0 + 1) = 6
          i     [(2,0)]  res = 2 * (3 - 0 + 1) = 8
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Edge cases
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        stack = [(heights[0], 0)]   # (height, left index)
        result = 0
        
        for i in range(1, len(heights)):
            curr, right = heights[i], i    # current number and right index
            peek, left = stack[len(stack)-1][0], stack[len(stack)-1][1]    # peek number and left index
            
            # Greater, add to stack
            if curr > peek:
                stack.append((curr, right))
            
            # Equal, calculate area, and continue
            elif curr == peek:
                
                result = max(result, peek * (right - left + 1))
                
            # Less, pop, then continuously calculate area, remove from stack until greater or empty stack
            else:
                stack.pop()
                
                while curr < peek:
                    result = max(result, peek * (right - left))
                    
                    # We want to keep the leftmost valid index for the current height, which occurs when curr >= peek or empty stack
                    previous_left = left  

                    if not stack:
                        stack.append((heights[i], previous_left))
                        break
                        
                    peek, left = stack[len(stack)-1][0], stack[len(stack)-1][1]    # update peak and left
                    
                    if curr >= peek:
                        stack.append((heights[i], previous_left))
                        break
                        
                    stack.pop()

        # At the end, we need to pop remaining numbers in stack which should descend in value and left index.
        # With value and left index, we can calculate additional areas
        while stack:
            peek, left = stack.pop()
            result = max(result, peek * (right - left + 1))
                    
        return result