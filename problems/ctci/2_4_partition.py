"""
https://quastor.org/cracking-the-coding-interview/linked-lists/partition

You are given an unsorted linked list and an integer (we'll call this the key). Write a function that partitions the linked list around the key. 
All the nodes with values that are less than the key will come before all the nodes with values that are greater than or equal to the key.

Input - 5 -> 6 -> 3 -> 5 -> 4 -> 10 -> None, key = 4
Output - 3 -> 5 -> 6 -> 5 -> 4 -> 10 -> None

The order of the nodes on either side of the partition doesn't matter.
"""
from email import headerregistry


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def partitionList(self, head, key):
        """
        This is very easy with O(n) time and O(n) space. You can use a queue and append left when curr.val < key and append right when curr.val >= key.

        When attempting to optimize further for O(1) space, you are left with only using the existing linked list.

        5 6 [3] 3 5 4 1, key = 4
        p c
          p  c  n       n = c.n, p.next = n, c.next = head, head = c, c = n   

        [3]-->5 6-->3 5 4 1
         c    h p   n          h = c, c = n  
         h          c     
        3 5 6 [3] 5 4 1    repeat
            p c
            p    c.n

        """
        # Edge case, if length 1, return list
        if not head.next:
            return head

        # We start prev at head and curr at head.next
        prev = head
        curr = head.next

        i = 0
        while curr:
            # Traverse prev and curr, until prev is >= key
            if prev.val < key:
                prev = curr
                curr = curr.next

            # If less than key, we move to front
            elif curr.val < key:
                
                next = curr.next
                prev.next = next   # skip current node
                curr.next = head   # append current node to head 

                # Update head and curr
                head = curr
                curr = next

            # Otherwise, keep traversing
            else:
                prev = curr
                curr = curr.next

            i += 1

        print(head.val)    
        return head

if __name__ == '__main__':
    def printList(curr):
        while curr:
            print(curr.val, end = " ")
            curr = curr.next
    f = ListNode(1)
    e = ListNode(4, f)
    d = ListNode(5, e)
    c = ListNode(3, d)
    b = ListNode(3, c)
    a = ListNode(6, b)
    head = ListNode(5, a)

    print("Key == 4 for 5633541.\nBefore:")
    printList(head)
    result = Solution().partitionList(head, 4)
    print("After:")
    printList(result)

    e = ListNode(4)
    d = ListNode(3, e)
    c = ListNode(1, d)
    b = ListNode(2, c)
    a = ListNode(5, b)
    head = ListNode(7, a)

    print("Key == 3 for 752134:\nBefore:")
    printList(head)
    result = Solution().partitionList(head, 4)
    print("After:")
    printList(result)