"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

BST equivalent at https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
The same solution works, although there is a more optimized approach with BST.
"""
from node_tree import TreeNode
class Solution:
    """
    https://jamboard.google.com/d/1EGspHSFDs5WNZ8JFHbgqk78TOWo6SvlWPzBsCUa6WT8/viewer

    Given constraints:
    1. All nodes have unique values
    2. p.val != q.val
    3. p and q both exist in Tree
    """
    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            while root:
                if root.val > p.val and root.val > q.val:
                    root = root.left
                elif root.val < p.val and root.val < q.val:
                    root = root.right
                else:
                    return root