class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self, head, n=None):
        if n == None:  # Traverse once
            head = head.next
            return head
        else:  # Traverse N times
            for i in range(0,n):
                head = head.next
            return head

    def insert_node(self, new, head, n=None):
        curr = head
        if n == None:  # Insert Front
            head = new
            head.next = curr
        else:
            for i in range(0, n):
                curr = curr.next
            N = curr.next
            curr.next = new
            new.next = N
        return head

    def delete_node(self, head, n=None):
        curr = head
        if n == None:
            head = head.next
        else:
            for i in range(0,n):
                curr = curr.next
            N = curr.next.next
            curr.next = N
        return head

    def append_node(self, new, head):
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new
        return head

    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
# Driver code
# if __name__ == '__main__':
#     # Starting List
#     n1 = ListNode(1)
#     n2 = ListNode(2)
#     n3 = ListNode(3)
#     n1.next = n2
#     n2.next = n3
#     head = n1
#     print("Starting list")
#     printList(head)
#
#     # Traverse Node
#     curr = traverse(head)
#     print("Traverse once")
#     printList(curr)
#
#     # Traverse Node Twice
#     curr = traverse(head, 2)
#     print("Traverse twice")
#     printList(curr)
#
#     # Insert Node in front
#     print("Inserting Node in front")
#     printList(insertNode(ListNode(0), head))
#
#     # Insert Node in index 1
#     print("Inserting Node in front of 1st element")
#     printList(insertNode(ListNode(0), head, 0))
#
#     # Append Node
#     print("Appending Node")
#     printList(appendNode(ListNode(0), head))
#
#     # Delete Node
#     print("Deleting Node in front of 1st element")
#     printList(deleteNode(head, 0))