"""
https://leetcode.com/problems/asteroid-collision/
"""
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=LN7KjRszjk4

    Think of the array is a 1D axis with asteroids on it. With the following details:
        (+) means right, (-) means left
        number == size
        bigger size, destroys smaller size
        same size destroys both

    Key thing to notice is we can use a stack to collect all positive asteroids. When a negative astroid comes, we need to consider the possiblility of the negative asteroid being bigger than subsequent positive asteroids collected in the stack.
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for asteroid in asteroids:
            # If positive, add to stack and result
            if asteroid > 0:
                stack.append(asteroid)
                result.append(asteroid)
            
            # If negative, you'll compare colliding asteroids
            elif asteroid < 0:
                negative = asteroid
                
                # Populated stack, means there are positive asteroids, collision will occur
                if stack:
                    positive = stack[len(stack) - 1]
                    
                    # If negative, we'll destroy all positives if positive < negative
                    while abs(positive) < abs(negative):
                        stack.pop()
                        result.pop()  # left destroyed
                        if not stack:
                            break
                        positive = stack[len(stack) - 1]
                        
                    # If positive > negative, we just destroy negative and move to next
                    if abs(positive) > abs(negative):
                        continue    # right destroyed
                        
                    # If negative == positive, we just destroy both and move to next
                    if abs(positive) == abs(negative):
                        stack.pop()  
                        result.pop()  # left destroyed
                        continue    # right destroyed
                
                # Empty stack, means there are no positive asteroids, so adding negative asteroid to result
                if not stack:
                    result.append(negative)
        return result
        