"""
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""
from node_list import ListNode
class Solution:
    def insert(self, head: 'ListNode', insertVal: int) -> 'ListNode':
        insert_node = ListNode(insertVal, None)

        # If empty head
        if not head:
            insert_node.next = insert_node
            return insert_node

        # If head of size 1
        if head.next == head:
            insert_node.next = head
            head.next = insert_node
            return head

        prev = head
        curr = head.next
        while curr:
            # Case 1: In between prev and curr, where prev < insertVal and curr > insertVal.
            if curr.val >= insert_node.val and prev.val <= insert_node.val:
                prev.next = insert_node
                insert_node.next = curr
                break

            # Case 2: In between max and min, where curr < prev, then you know you reached the max because it is already sorted.
            elif curr.val < prev.val:
                if (curr.val >= insert_node.val and prev.val >= insert_node.val) or (
                        curr.val <= insert_node.val and prev.val <= insert_node.val):
                    prev.next = insert_node
                    insert_node.next = curr
                    break

            # Traverse prev and curr
            prev = curr
            curr = curr.next

            # Case 3: Did not insert in loop, then break
            if prev == head:
                break

        prev.next = insert_node
        insert_node.next = curr
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    head.next.next.next = head

    curr = Solution().insert(head, insertVal=5)

    print("Printing Linked List:")
    seen = set()
    while curr and curr not in seen:
        seen.add(curr)
        print(curr.val)
        curr = curr.next

