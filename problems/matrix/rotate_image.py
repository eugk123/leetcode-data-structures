def rotateEugene(matrix):
    """
    https://leetcode.com/problems/rotate-image/

    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
    another 2D matrix and do the rotation.

    123    741
    456 -> 852
    789    963

    Example:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Initiution: Since this is a SQUARE matrix, we can store 4 corners first in temp list, then rotate.
    Iterate to next index, and repeat.

    Complexity:
    Time: O(n^2) since two inserted loops
    Space: O(1)

    Speed: 36ms 54% same as LeetCode Solution

    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix_length = len(matrix)
    last_index = len(matrix) - 1
    first_index = 0
    matrix_layers = len(matrix)-2

    if matrix is []:
        return
    if matrix_length == 1:
        return matrix
    if matrix_length == 2:
        matrix_layers = len(matrix)-1
    for j in range(matrix_layers):
        for i in range(matrix_length - 1):
            tmp = []  # Empty tmp storage
            # Store
            tmp.append(matrix[first_index + j][i + j])  # Store first element of first row
            tmp.append(matrix[i + j][last_index - j])  # Store first element of last column
            tmp.append(matrix[last_index - j][last_index - i - j])  # Store first element of reverse(last row)
            tmp.append(matrix[last_index - i - j][first_index + j])  # Store first element of reverse(first column)

            # Traverse
            matrix[i + j][last_index - j] = tmp[0]  # Traverse first row element to last column element
            matrix[last_index - j][last_index - i - j] = tmp[1]  # Traverse last column element to reverse(last row) element
            matrix[last_index - i - j][first_index + j] = tmp[2]  # Traverse reverse(last row) element to reverse(first column) element
            matrix[first_index + j][i + j] = tmp[3]  # Traverse reverse(first column) element to first row element
        matrix_length-=2
    print(matrix)


def rotate_sequential(matrix):
    matrix_length = len(matrix)
    last_index = len(matrix) - 1
    first_index = 0

    j=0
    for i in range(matrix_length - 1):
        tmp = []  # Empty tmp storage

        # Store
        tmp.append(matrix[first_index + j][i + j])  # Store first element of first row
        tmp.append(matrix[i + j][last_index - j])  # Store first element of last column
        tmp.append(matrix[last_index - j][last_index - i - j])  # Store first element of reverse(last row)
        tmp.append(matrix[last_index - i - j][first_index + j])  # Store first element of reverse(first column)

        # Traverse
        matrix[i + j][last_index - j] = tmp[0]  # Traverse first row element to last column element
        matrix[last_index - j][last_index - i - j] = tmp[1]  # Traverse last column element to reverse(last row) element
        matrix[last_index - i - j][first_index + j] = tmp[2]  # Traverse reverse(last row) element to reverse(first column) element
        matrix[first_index + j][i + j] = tmp[3]  # Traverse reverse(first column) element to first row element

    j=1
    for i in range(matrix_length - 3):
        tmp = []  # Empty tmp storage

        # Store
        tmp.append(matrix[first_index + j][i + j])  # Store first element of first row
        tmp.append(matrix[i + j][last_index - j])  # Store first element of last column
        tmp.append(matrix[last_index - j][last_index - i - j])  # Store first element of reverse(last row)
        tmp.append(matrix[last_index - i - j][first_index + j])  # Store first element of reverse(first column)

        # Traverse
        matrix[i + j][last_index - j] = tmp[0]  # Traverse first row element to last column element
        matrix[last_index - j][last_index - i - j] = tmp[1]  # Traverse last column element to reverse(last row) element
        matrix[last_index - i - j][first_index + j] = tmp[2]  # Traverse reverse(last row) element to reverse(first column) element
        matrix[first_index + j][i + j] = tmp[3]  # Traverse reverse(first column) element to first row element
    print(matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[ 1, 2, 3, 4],
              [ 5, 6, 7, 8],
              [ 9,10,11,12],
              [13,14,15,16]]
    matrix3 = [[1,2],[3,4]]

    print("Case 1, 3x3:")
    rotateEugene(matrix1)
    print("Case 2, 4x4:")
    rotateEugene(matrix2)
    print("Case 3, 2x2:")
    rotateEugene(matrix3)



