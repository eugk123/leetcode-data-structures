class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.tail = 0
        self.head = 0
        self.size = 0
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.length:
            return False
        elif self.size == 0:
            self.tail = self.head = 0
            self.queue[0] = value
        else:
            self.queue[self.head] = value
        self.head += 1
        self.head = self.head % self.length
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            self.tail = self.head = 0
            return False
        else:
            self.queue[self.tail] = 0

        self.tail += 1
        self.tail = self.tail % self.length
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.tail]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.head - 1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.length:
            return True
        return False

if __name__ == '__main__':
    queue = MyCircularQueue(3)
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(3)
    queue.enQueue(4)
    print(queue.Rear())
    print(queue.Front())
    queue.isFull()
    queue.deQueue()
    queue.enQueue(4)
    print(queue.Rear())
    print(queue.Front())
