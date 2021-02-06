"""
https://leetcode.com/problems/palindrome-linked-list/
"""
from node_list import ListNode
class Solution:
    """
    Easy way is to use a list to determine if linked list is palindrome.

    A space efficient solution is more difficult. Figure out how long the list is. Figure out if odd or even to determine
    1 or 2 mid nodes. Reverse linked list halfway. Then Traverse outwards.
    O(n) time and O(1) space solution
    """

    class Solution:
        def isPalindrome(self, head: ListNode) -> bool:
            if head is None:
                return True
            if head.next is None:
                return True

            tail = head  # Used find end
            count = 1  # Total count of nodes
            isOdd = False  # Determines if even or odd number of nodes

            while tail.next:
                tail = tail.next
                count = count + 1

            if count % 2 == 1:
                isOdd = True  # 3/2 + 1 = 1 + 1 -> 2
                midCount = int(count / 2) + 1
            else:
                midCount = int(count / 2)  # 4/2 = 2 -> 2 & 3 duplicates

            # Reverse halfway
            print(count, midCount)
            prev = None
            curr = head
            count = 0
            while curr and count < midCount:
                N = curr.next  # store next pointer
                curr.next = prev  # Reverse pointer
                prev = curr  # Traverse prev
                curr = N  # Traverse curr
                count += 1
            print(prev.val, curr.val, isOdd)
            if isOdd:
                # Odd case, same middle, traverse once on left pointer
                right = curr
                left = prev.next
            else:
                # Even case, left is prev, right is final N pointer
                right = curr
                left = prev

            while left:
                # If one side is null, then false
                if left is None and right:
                    return False
                if right is None and left:
                    return False

                # If equal, the continue
                if left.val == right.val:
                    left = left.next
                    right = right.next
                else:
                    # Not equal, obviously False
                    return False

            # Completed everything? Then Palidrome!
            return True



