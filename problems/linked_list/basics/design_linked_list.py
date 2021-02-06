"""
https://leetcode.com/problems/design-linked-list/submissions/
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # If index = 0, return head
        if index == 0:
            return self.head.val

        # Start traversing for index > 0
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1  # We decrement index to stop at desired index
            if not curr:
                return -1  # Return -1 when end of ll is reached
        return curr.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head is None:
            # New node is head
            self.head = node
        else:
            # New node points to head, update head
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head is None:
            # New node is head
            self.head = node
        else:
            # Traverse to end. Point end to new node
            curr = self.head
            while curr.next:  # Why curr.next? Because if we do while curr, curr will traverse until it points to None.
                curr = curr.next
            curr.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node(val)

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head

            # We want to insert behind desired index.
            while index > 1:
                curr = curr.next
                index -= 1
            temp = curr.next  # Store the next
            node.next = temp  # Point node to next
            curr.next = node  # Point prev to node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0 and not self.head.next:
            # If index = 0 and only 1 node
            self.head = None
            return
        elif index == 0:
            # If index = 0, update head
            self.head = self.head.next
            return


        # Start traversing for index > 0, store previous and have previous skip to curr.next.next
        curr = self.head
        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1  # We decrement index to stop at desired index
            if not curr:
                return  # Return when end of ll is reached -- meaning nothing to delete or repoint.
        prev.next = curr.next

if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(2)
    ll.addAtHead(3)
    ll.addAtTail(15)
    ll.addAtIndex(1, 1)
    ll.deleteAtIndex(1)

    curr = ll.head
    while curr is not None:
        print(curr.val)
        curr = curr.next

