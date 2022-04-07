"""
https://leetcode.com/problems/find-the-duplicate-number
"""
class Solution:
    """
    Similar to Linked List Cycle. Watch Neetcode
    https://www.youtube.com/watch?v=wjYnzkAhcNk
    
    1 -> 3 -> 2 -> 4 -> 2 
    
    start slow and fast at 0th index
    Traverse fast pointer twice and slow pointer once
    0 1 2 3 4
    1 3 4 2 2
    sf
    s f
        sf    -> intersection index found at index 2
    
    start slow1 at intersected index and slow2 at 0
    Traverse until they intersect
    0 1 2 3 4
    1 3 4 2 2
    s1  s2
    s1    s2
        s2s1
            ss   -> intersection index found at index 4   
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1, slow and fast pointer both starting at beginning
        # move 1 by 1 for slow and 2 by 2 for fast
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
            if slow == fast:
                break
        
        # phase 2, start at beginning and start at intersection,
        # move 1 by 1 for both till intersect
        slow1, slow2 = nums[0], slow
        while True:
            if slow1 == slow2:
                return slow1
            slow1 = nums[slow1]
            slow2 = nums[slow2]
