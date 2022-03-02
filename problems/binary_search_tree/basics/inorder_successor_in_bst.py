"""
https://leetcode.com/problems/inorder-successor-in-bst
"""
from node.node_tree import TreeNode
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs_in_order(node):

            if node.left:
                dfs_in_order(node.left)

            # check if prev == p, then update the current node!
            if self.prev == p:
                self.curr = node

            # update prev
            self.prev = node

            if node.right:
                dfs_in_order(node.right)

        # instantiate prev and curr pointers
        self.prev = None
        self.curr = None

        dfs_in_order(root)

        # return current node
        return self.curr
