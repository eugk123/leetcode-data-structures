def containsDuplicate(nums):  # Heapsort Algorithm
    """
    https://leetcode.com/problems/contains-duplicate/

    Your function should return true if any value appears at least twice in the array, and it should return false if
    every element is distinct.

    Example:
    Input: [1,2,3,1]
    Output: true

    Complexity:
    Time Complexity: O(n logn). This approach employs sorting algorithm. Since comparison sorting algorithm like
    heapsort is known to provide O(n logn) worst-case performance, sorting is often a good preprocessing step.
    After sorting, we can sweep the sorted array to find if there are any two consecutive duplicate elements.
    Space Complexity: O(1). Heapsort

    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()  # Sort the Array
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i+1]:  # Check if current and next number are equal!
            return True
    return False  # Otherwise return false

def containsDuplicates_HashSet(nums):  # Hash Set
    duplicates = set()
    for num in nums:
        duplicates.add(num)
    if len(nums) > len(duplicates):
        return True
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(containsDuplicate([7, 2, 1, 3, 4, 1]))