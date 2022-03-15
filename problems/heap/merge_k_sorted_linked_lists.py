"""
https://leetcode.com/problems/merge-k-sorted-lists

**There is a linked list type solution under the linked list section
"""
import collections
class Solution:
    """
    Heap Solution

    1. Create min_heap and add all nodes using tuple (val, node) to sort on value. At every iteration, make sure to detach previous node.
    2. Continuously heappop from min_heap and create sorted linked list

    If receiving TypeError, consider using a hash_map that stores index to node with touple (val, index)

    Time O(NlogN) - heap operations is O(log N) and iterating N times totals to O(NlogN)
    """
    def mergeKListsIndexMap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index_to_node = {}  # Need this index map because of TypeError
        min_heap = []
        i = 0
        for curr in lists:
            if not curr:
                continue
                
            while curr:
                heapq.heappush(min_heap, (curr.val, i))
                index_to_node[i] = curr  # store index to node
                # detach previous and traverse current
                # to prevent cycle
                prev = curr
                curr = curr.next
                prev.next = None
                i += 1

        if not min_heap:
            return None

        prev_i = heapq.heappop(min_heap)[1]
        prev = index_to_node[prev_i]  # get node using index
        head = prev
        
        while min_heap:
            curr_i = heapq.heappop(min_heap)[1]  
            curr = index_to_node[curr_i]  # get node using index

            # attach previous to current
            prev.next = curr
            prev = curr
            
        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # this one liner below is needed for Python3 to fix TypeError
        # https://leetcode.com/problems/merge-k-sorted-lists/discuss/465094/Problems-with-Python3-and-Multiple-Solutions
        ListNode.__lt__ = lambda self, other: self.val < other.val        

        min_heap = []
        for curr in lists:
            if not curr:
                continue
                
            while curr:
                heapq.heappush(min_heap, (curr.val, curr))
                
                # detach previous and traverse current
                # to prevent cycle
                prev = curr
                curr = curr.next
                prev.next = None

        if not min_heap:
            return None

        prev = heapq.heappop(min_heap)[1]
        head = prev
        
        while min_heap:
            curr = heapq.heappop(min_heap)[1]
            
            # attach previous to current
            prev.next = curr
            prev = curr
            
        return head
