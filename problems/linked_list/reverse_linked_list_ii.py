from node_list import ListNode
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseList(head):
            # x  1 2 3
            # p  c n
            #    p c
            curr = head
            prev = None
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            left = prev
            right = head
            return left, right
        
        # left_edge, left_current, r_current, right_edge
        # 1 -> 2 -> 3 -> 4 -> 5, l=2, r=4
        # le   lc        rc   re
        
        curr = head
        left_edge = None
        left_current = None
        right_edge = None
        right_current = None
        
        # First pass, set pointers
        i = 1
        while curr:
            if i == left - 1:
                left_edge = curr
            if i == left:
                left_current = curr
            if i == right:
                right_current = curr
            if i == right + 1:
                right_edge = curr
            
            curr = curr.next
            i += 1

        # print(left_current.val, right_current.val, right_edge.val)
        # Detach left
        if left_edge:
            left_edge.next = None
        
        # Detach right
        if right_edge:
            right_current.next = None
        
        # Reverse in between
        left_current, right_current = reverseList(left_current)
        
        
        # Attach left
        if left_edge:
            left_edge.next = left_current
        else:
            # In the event where left_current is the first node, we need to reset head here.
            head = left_current
            
        # Attach right
        if right_edge:
            right_current.next = right_edge
         
        return head