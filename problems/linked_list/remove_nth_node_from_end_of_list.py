from node.node_list import ListNode
class Solution:
    def removeNthFromEnd(self, head, n): # Two Pass Algo
        """
        Two Pass Solution
        """
        curr = head
        l = 0
        while curr: # Find total length of linked list
            curr = curr.next
            l = l + 1
        if n == l: # Base case if n = l, this means remove first node.
            return head.next
        remove_index = l - n # Index of node to remove
        curr = head
        for i in range(1, remove_index): # Traverse to index of node to remove
            curr = curr.next
        curr.next = curr.next.next # Skip next node to remove that node
        return head

    def removeNthFromEnd_OnePass(self, head: ListNode, n: int) -> ListNode:
        """
        One Pass Solution:  https://www.youtube.com/watch?v=XVuQxVej6y8

        However, the time complexity of two pass is exactly the same though. O(2N-L) = O(N).
        """
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy

        # Base case, for len == 1
        if head.next is None:
            return None

        # Have the right pointer n nodes away from left
        for i in range(n):
            right = right.next

        # Traverse both pointers until right.next = null, then have the left
        while right.next is not None:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n1 = ListNode(1); n2 = ListNode(2); n3 = ListNode(3); n4 = ListNode(4); n5 = ListNode(5)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    head = n1

    print("Original Linked List:")
    head.print_list(head)

    print("\nResultant Linked List:")
    res_node = Solution().removeNthFromEnd_OnePass(head, 2)
    res_node.print_list(res_node)