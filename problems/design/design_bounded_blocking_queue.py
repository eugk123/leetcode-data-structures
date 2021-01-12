from collections import deque
import threading
class BoundedBlockingQueue(object):
    """
    https://leetcode.com/problems/design-bounded-blocking-queue/discuss/594080/DONT-USE-THE-THREAD-SAFE-Collections.deque-during-interviews!!!!

    Not sure if we can use the deque object or not. Would like to wait for more updates on this solution.
    """
    def __init__(self, capacity):
        self.capacity = capacity

    def enqueue(self, element):
        """
        Adds an element to the front of the queue.

        If the queue is full, the calling thread is blocked until the queue is no longer full.
        """
        queue.append(element)


    def dequeue(self):
        """
        Returns the element at the rear of the queue and removes it.

        If the queue is ending the calling thread is blocked until the queue is no longer empty.
        """
        return

    def size(self, queue):
        """
        Returns number of elements currently in the queue
        """
        return len(queue)

if __name__ == '__main__':
    queue = BoundedBlockingQueue(5)
    print(queue.enqueue(1))