"""
https://www.geeksforgeeks.org/stack-data-structure-introduction-program/#:~:text=%20There%20are%20two%20ways%20to%20implement%20a,Using%20array%202%20Using%20linked%20list%20More%20

Stack is a linear data structure that follows a particular order in which the operations are performed.

Design operations:
    Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
    Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
    Peek or Top: Returns the top element of the stack.
    isEmpty: Returns true if the stack is empty, else false.

Can implement in either linked list or dynamic array. For a basic stack, it's recommended to use a linked list because the append is O(1) constant time. Lookups will only be performed at the top too which is always O(1).
In contrast, a dynamic array needs to resize when exceeding initial capacity; therefore, appending has a worst cast of O(n) time.

Problems to try:
https://leetcode.com/problems/min-stack/
https://leetcode.com/problems/max-stack/
"""
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self):
        self.stack = None

    def push(self, val: int):
        if not self.stack:
            self.stack = ListNode(val)
        else:
            new_node = ListNode(val)
            new_node.prev = self.stack  # attach prev
            self.stack.next = new_node  # attach next
            self.stack = self.stack.next  # traverse next

    def pop(self):
        # Edge case, should skip if empty
        if not self.stack:
            return

        # Should skip via prev pointer if list has more than one number
        if self.stack.prev:
            self.stack = self.stack.prev  # move backwards
            self.stack.next = None  # remove end
        
        # Othersie, only one node left, make empty
        else:
            self.stack = None


    def is_empty(self):
        if self.stack:
            return False
        return True
    
    def peek(self):
        if self.stack:
            return self.stack.val

if __name__ == '__main__':
    stack = Stack()
    print("Is stack empty?: {}".format(stack.is_empty()))
    stack.push(3)
    print("Pushed {}".format(stack.peek()))
    stack.push(15)
    print("Pushed {}".format(stack.peek()))
    stack.push(-5)
    print("Pushed {}".format(stack.peek()))
    print("Is stack empty?: {}".format(stack.is_empty()))
    stack.pop()
    print("Popped! So current number should be same as second push: {}".format(stack.peek()))
    stack.pop()
    print("Popped! So current number should be same as first push: {}".format(stack.peek()))
    stack.pop()
    print("Popped! Should be empty now: {}".format(stack.peek()))
    stack.pop()
    print("Can't pop, should be empty: {}".format(stack.peek()))
    print("Is stack empty?: {}".format(stack.is_empty()))
