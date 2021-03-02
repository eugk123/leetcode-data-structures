class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # If k == len or len(arr) == 1, return arr
        if k == len(arr) or len(arr) == 1:
            return arr

        # Edge Case: If target is out of bounds, we know to return either the first or last index.
        target = x
        if target > arr[len(arr) - 1]:
            index = len(arr) - 1
        elif target < arr[0]:
            index = 0

        # If target is in the array or inbetween two elements, we know we can perform binary search.
        else:
            # Perform simple binary search to grab index for target "x"
            left, right = 0, len(arr) - 1
            while left <= right:

                mid = left + (right - left) // 2

                # Attempt to look for target
                if arr[mid] == target:
                    index = mid
                    break

                # Edge Case: If target is between two numbers,
                # return the closer number
                # return the leftmost index if distance is same
                if arr[mid] < target and target < arr[mid + 1] and mid < len(arr) - 1:
                    # Return rightmost if following condition is met.
                    if target - arr[mid] > arr[mid + 1] - target:
                        index = mid + 1
                        break
                    # Otherwise leftmost is returned.
                    index = mid
                    break

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        # Starting at the mid pointer, traverse to a width of k while satisfing the "closest k" condition
        left = index
        right = index

        # Left has priority even if distance is the same.
        #
        # Ex: for [1,2,3,4,5] with k = 2 and x = 2, the res = [1,2] not [2,3].
        distance = 0  # Start with distance 0
        while right - left < k:
            # Break out of the while loop when right - left + 1 == k
            if right - left + 1 == k:
                break

            # Use continue to not skip distance until all shortest distances are found.
            if left > 0 and target - arr[left - 1] == distance:
                left -= 1
                continue
            if right < len(arr) - 1 and arr[right + 1] - target == distance:
                right += 1
                continue

            # Expand distance by 1
            distance += 1

        return arr[left:right + 1]