"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
import math
from node_tree import TreeNode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs_in_order(node):
            if not node:
                return

            if dfs_in_order(node.left) is False:
                return False

            # In-order traversal property in BST is that the value of nodes are in ascending order
            # Using recursion, you can grab the next node in between left and right recursive calls!
            # Check the previous value with the current.
            if node.val <= self.prev:
                return False
            else:
                self.prev = node.val

            if dfs_in_order(node.right) is False:
                return False

            return True

        self.prev = -math.inf
        return dfs_in_order(root)


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)

    print(Solution().isValidBST(node))