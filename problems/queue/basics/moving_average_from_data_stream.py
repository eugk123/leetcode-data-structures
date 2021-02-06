"""
https://leetcode.com/problems/moving-average-from-data-stream
"""
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        """
        
        """
        if len(self.queue) == self.size:
            front_val = self.queue.popleft()
            self.total = self.total - front_val
        self.queue.append(val)
        self.total = self.total + val
        average = self.total / len(self.queue)
        return average



if __name__ == '__main__':
    queue = MovingAverage(5)
    print(queue.next(5))
    print(queue.next(55))
