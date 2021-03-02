"""
https://leetcode.com/problems/inorder-successor-in-bst-ii
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    """
    https://www.youtube.com/watch?v=5zgytmvJ3Mg
    https://jamboard.google.com/d/13oXkI7NiyvWXLoKNyMwN0tDLdMhIp2kZ6vRCJrtO6lg/viewer?f=0
    """
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # In BST, next successor is going to be towards the children path (first right) before the parent path
        # When taking children path, you need to check the right. The left path will be invalid.
        # After traversing right, that could be the valid successor, but a closer in value successor will be on the far leftmost child
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # When taking parent path, you need to check the right since that will be your next closest successor. If not right, but left exists, traverse left over and over again until a right path is available. Now if no path is found, return None
        # To make this easier, you don't really have to check directions since we are given a valid BST. We could just use the values to verify. If the value is indeed greater, we know it's the right parent node. You need to first store the initial node value
        value = node.val
        while node.parent:
            node = node.parent

            if value < node.val:
                return node
        return None