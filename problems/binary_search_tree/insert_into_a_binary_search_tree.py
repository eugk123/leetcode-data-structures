"""
https://leetcode.com/problems/insert-into-a-binary-search-tree
"""
from node_tree import TreeNode
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root, node):

            # Check left
            if node.val < root.val:
                if not root.left:
                    root.left = node
                elif root.left:
                    insert(root.left, node)

            # Check right
            if node.val > root.val:
                if not root.right:
                    root.right = node
                elif root.right:
                    insert(root.right, node)

            return

        node = TreeNode(val)

        if not root:
            return node

        insert(root, node)

        return root