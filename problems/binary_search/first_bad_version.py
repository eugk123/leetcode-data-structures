# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    Binary Search

    In the interview, the interviewer will be clear if there is a more efficient solution than brute force linear, which there is. In that case, a binary search is needed.

    Binary search can be performed on a range of numbers. It does not have to be an array! The edge case in this problem is isBadVersion(1) because the search definition will not be able to check the first version.

    We want to find the inflection point where the version is good and then the next version is bad. That will be the return condition.

    Time O(n)
    Space O(1)

    Note: Cannot get this running in visual studio code. The intent of this problem is that we don't actually know which version is the bad version.
    """
    def firstBadVersion(self, n: int) -> int:
        # Edge case
        if isBadVersion(1):
            return 1
        
        left = 1
        right = n
        while left <= right:
            middle = int(left + (right - left)/2)
            
            if not isBadVersion(middle) and isBadVersion(middle + 1):
                return middle + 1
            
            if not isBadVersion(middle):
                left = middle + 1
            else:
                right = middle - 1