from node_list import ListNode
class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list
    """
    def reverse(self, node: ListNode) -> ListNode:
        prev = None
        curr = node
        while curr:
            temp = curr.next  # Store curr.next
            curr.next = prev  # Point curr to previous for reversing.
            prev = curr  # Traverse prev
            curr = temp  # Traverse curr
        return curr

    def reverse_recursive(self, node):
        """
        https://www.youtube.com/watch?v=MRe3UsRadKw&feature=emb_title
        """
        if not node or not node.next:
            return node
        p = self.reverse_recursive(node.next)  # We pass in node.next because we want the reversal to occur one node before.
        node.next.next = node
        node.next = None
        return p  # return this last, not at the recursive calls, so we can redirect pointers

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    curr = Solution().reverse_recursive(node = n1)

    print("Original Linked List:")
    n1.print_list(n1)

    print("\nReversed Linked List:")
    curr.print_list(curr)
