from datetime import datetime
def binary_search_iterative(nums, x):
    """
    Returns True if x is found. False if not found

    Time complexity: O(log n)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        # Update mid pointer (cast to int - this will floor floats)
        mid = int(left + (right - left) / 2)

        # Closure condition
        if nums[mid] == x:
            return True

        # Condition to update left or right pointer. This works only for sorted array.
        elif x < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

def linear_search_iterative(nums, x):
    for num in nums:
        if num == x:
            return True
    return False

if __name__ == '__main__':
    arr = [0] * 50000    # The more elements, the faster binary search is
    arr.append(3)
    x = 3

    start = datetime.now()
    print(binary_search_iterative(arr, x))
    print("Binary Search Time: {}".format(datetime.now() - start))


    start = datetime.now()
    print(linear_search_iterative(arr, x))
    print("Linear Search Time: {}".format(datetime.now() - start))