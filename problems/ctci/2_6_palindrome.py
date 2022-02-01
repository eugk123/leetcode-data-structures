"""
https://quastor.org/cracking-the-coding-interview/linked-lists/return-kth-to-last

You are given a linked list. Write a function that checks if the values in the linked list will form a palindrome. In other words, if you reverse the linked list, the values will still be the same.

Input - 1 -> 2 -> 2 -> 1
Output - True

Input - 1 -> 2 -> 3 -> 2 -> 1
Output - True

Input - 1 -> 2
Output - False
"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        """
        One pass with stack

        Use slow and fast pointer, add to stack, determine if even or odd length.
        Once fast pointer reaches end, continue with slow pointer and see if contents match stack.

        odd         even
        1234321     123321
           s          s
              f         f
        
        stack
        [1,2,3,4]   [1,2,3]
        stay        move s by 1

        Time Complexity: O(n)
        Space Complexity: O(n)

        To further optimize, you could reverse from slow pointer to tail. Then compare head and tail and work inwards. This would achieve O(1) space.
        """
        slow = fast = head
        
        # We want to position the slow pointer right in the middle
        stack = []
        count = 1
        while fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            count += 2
            if not fast.next:
                break
            if not fast.next.next:
                count += 1
                break
        stack.append(slow.val)

        # Check odd or even
        # 4/2 = 3       5/2 = 2
        # (4+1)/2 = 3   (5+1)/2 = 3
        # 3 == 3: even  2 != 3: odd 
        if int(count/2) == int((count + 1)/2):
            # even, so we just traverse the slow pointer one time.
            slow = slow.next
            
        
        while slow:
            if slow.val == stack.pop():
                slow = slow.next
                continue
            else:
                return False
        
        return True

if __name__ == '__main__':

    f = ListNode(1)
    e = ListNode(2, f)
    d = ListNode(3, e)
    c = ListNode(4, d)
    b = ListNode(3, c)
    a = ListNode(2, b)
    head = ListNode(1, a)

    print("1234321: {}".format(Solution().isPalindrome(head)))

    e = ListNode(1)
    d = ListNode(2, e)
    c = ListNode(3, d)
    b = ListNode(3, c)
    a = ListNode(2, b)
    head = ListNode(1, a)

    print("123321: {}".format(Solution().isPalindrome(head)))