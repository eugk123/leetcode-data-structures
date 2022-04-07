"""
Asked in capital one assessment

Blocks shown as "F" in a matrix fall and stop at hashtags "#". Given an input matrix, return the resulting configuration.

FF.    ...
.F. -> FF.
#..    #F.
...    ...
"""
import math
from typing import List
def gravity_problem(matrix: List[int]):
    
    # First populate a hash map containing last_seen_block[i] -> j. This needs to be the last "F" that is above the hashtag.
    # So we need a condition to check -> if j not in first_seen_hashtag.

    # Populate a hash map containing first_seen_hashtag[i] -> j
    last_seen_block = {}
    first_seen_hashtag = {}
    for i in range(len(matrix)):

        for j in range(len(matrix[0])):
            if matrix[i][j] == "F" and j not in first_seen_hashtag:
                last_seen_block[j] = i

            if matrix[i][j] == "#":
                first_seen_hashtag[j] = i
                
    # We traverse through each key in first_seen_hashtag to calculate shortest vertical distance between hashtag and "F".
    shortest_distance = math.inf
    for j in first_seen_hashtag:
        shortest_distance = min(shortest_distance, first_seen_hashtag[j] - last_seen_block[j] - 1)

    # Then we update the matrix in reverse order by shifting all "F" down by shortest calculated distance
    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[0]))):
            # print(i, j)
            if matrix[i][j] == "F":
                matrix[i][j] = "."
                matrix[i+shortest_distance][j] = "F"

    return matrix


if __name__ == "__main__":

    matrix =[["F","F","."],[".","F","."],["#",".","."],[".",".","."]]
    print(gravity_problem(matrix))