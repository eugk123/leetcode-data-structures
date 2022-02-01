"""
https://leetcode.com/problems/design-circular-queue/
https://www.geeksforgeeks.org/implementation-deque-using-circular-array/

Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

Design operations:
    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

The confusing part of this problem is understanding what front and rear means. It wasn't clear, as I got it switched.
Front is the first element added to the queue. Rear is the last element added to the queue.

[fr| | ]    MyCircularQueue(3)
[1fr| | ]   enQueue(1) - empty capacity, add via rear
[1f|2r| ]   enQueue(2) - traverse then add via rear
[1f|2|3r]   enQueue(3) - traverse then add via rear
[1f|2|3r]   enQueue(4) - full capacity, do nothing
[ |2f|3r]   deQueue() - remove via front then traverse, Rear() -> 3, Front() -> 2 
[ | |3fr]   deQueue() - remove via front then traverse
[ | |fr]    deQueue() - remove via front, don't traverse since empty
[fr| | ]   deQueue() - empty capacity, reset pointers
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.total_capacity = k
        self.current_capacity = 0

    def enQueue(self, value: int) -> bool:
        # If it is empty, we simply just populate the current index
        if self.current_capacity == 0:
            self.queue[self.rear] = value
            self.current_capacity += 1
            return True
        
        # If it is full capacity, we don't do anything
        if self.current_capacity == self.total_capacity:
            return False
        
        # If capacity is not full or not empty, traverse then add
        else:
            # Traverse rear index
            self.rear += 1

            # We reached the end, and moving index back to 0
            if self.rear == self.total_capacity:
                self.rear = 0
            
            # Populate and update current capacity
            self.queue[self.rear] = value
            self.current_capacity += 1
            
            return True
    
    def deQueue(self) -> bool:
        # If it is empty, do nothing
        if self.current_capacity == 0:
            self.front = 0
            self.rear = 0
            return False
        
        # [1fr, ]
        # If capacity is not empty, remove then traverse
        else:
            # Remove and decrement current capacity
            self.queue[self.front] = None
            self.current_capacity -= 1
            
            # If capacity is not zero, then we keep traversing
            if self.current_capacity > 0:
                self.front += 1
                
                # If we reached the end, move index back to 0
                if self.front == self.total_capacity:
                    self.front = 0
            return True
            
    def Front(self) -> int:
        # [1f,2,3r] -> 1 was added first, so this is the front
        # Front is the first element added to the queue
        if self.queue[self.front] != None:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        # [1f,2,3r] -> 3 was added last, so this is the rear
        # Rear is the last element added to the queue
        if self.queue[self.rear] != None:
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        if self.current_capacity == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.current_capacity == self.total_capacity:
            return True
        return False