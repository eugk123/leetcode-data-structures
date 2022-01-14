"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.

        s1 [1], s2 [] -> s1 [], s2 [1]

        s1 [1 2], s2 [1] -> s1 [], s2 [2 1]
        """
        if self.s2:
            for i in range(len(self.s2)):
                item = self.s2.pop()
                self.s1.append(item)
            self.s2 = []
        self.s1.append(x)

        # You'll populate s2 by flipping s1
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        front = self.s2.pop()
        return front

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s2[len(self.s2) - 1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s2:
            return True
        else:
            return False

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(5)
    obj.pop()
    print(obj.peek())
    print(obj.empty())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()