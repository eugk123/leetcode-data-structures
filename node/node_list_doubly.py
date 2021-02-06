class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next