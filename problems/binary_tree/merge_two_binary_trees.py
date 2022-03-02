"""
https://leetcode.com/problems/merge-two-binary-trees/
"""
from node.node_tree import TreeNode
class Solution:
    """
    Most optimal is to update one of the trees to save space.

    Time: O(n + m)
    Space: O(max(n,m)) in case of a skewed tree - worst case.
    """
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(root1, root2):
            # We are updating root1 tree and returning that tree for optimized space.
            if root1 and root2:
                root1.val = root1.val + root2.val

            # If both left exists -> update left
            if root1.left and root2.left:
                dfs(root1.left, root2.left)

            # If both right exists -> right left
            if root1.right and root2.right:
                dfs(root1.right, root2.right)

            # If no right for root1, but right for root2, add root2.right to root1.right
            if not root1.right and root2.right:
                root1.right = root2.right

            # If no left for root1, but left for root2, add root2.left to root1.left
            if not root1.left and root2.left:
                root1.left = root2.left

        # Edge cases - only 1 exists, or both don't exist
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        if not root1 and not root2:
            return None

        # Simply execute recursive function to update root1
        dfs(root1, root2)
        return root1