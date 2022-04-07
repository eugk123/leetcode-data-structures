"""
Asked in capital one assessment

[1,2,3,4,5,2,7,8,9
 4,5,6,7,8,9,1,2,3,
 7,8,9,1,2,3,4,5,6]
     T,T,T,F,F,F,T
For every 3 by 3 matrix sliding to the right, how many 3x3 blocks can you find that have numbers 1~9.

Result matrix should have an array of True or False
"""

# Solution is to have a hash map that can contain numbers 1 through 9
# We first populate it with the initial block
# Then we use a left and right pointer to continually remove prev column and add new column
# After the remove and add, we check if the map contains all 9 numbers, if so we add True to the result, then traverse left and right.