"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from node_tree import TreeNode
class Solution:
    """
    Lowest common ancestor for two nodes p and q would be the last ancestor node common to both of them.
    Here last is defined in terms of the depth of the node. The below diagram would help in understanding what lowest means.

    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # In a BST, you know that traversals occur left-node-right in ascending order.
        while root:
            # Therefore, from the root, if both p and q are less than the root value,
            # we know that it's on the left side, so we traverse left
            if max(p.val, q.val) < root.val:
                root = root.left

            # Also, from the root, if both p and q are greater than the root value,
            # we know that it's on the right side, so we traverse right
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left.left = TreeNode(1)
    q = root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(0)

    print("Inorder print - ascending order verifies BST:")
    root.print_in_order(root)

    res = Solution().lowestCommonAncestor(root, p, q)
    print("\nResult common ancestor value: {}".format(res.val))