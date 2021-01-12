"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
import math
from node_tree import TreeNode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs_in_order(root):
            if root == None:
                return
            if not dfs_in_order(root.left):
                return False
            if self.prev is not None and root.val <= self.prev:
                return False
            self.prev = root.val
            return dfs_in_order(root.right)

        self.prev = -math.inf
        return dfs_in_order(root)

    def isValidBST_Eugene(self, root: TreeNode) -> bool:
        """
        Not optimal time and space since you're creating and searching an additional array of length N.
        """
        def dfs_in_order(root):
            if root == None:
                return
            dfs_in_order(root.left)
            nodes.append(root.val)
            dfs_in_order(root.right)

        nodes = []
        dfs_in_order(root)
        for i in range(len(nodes)):
            if i > 0 and nodes[i] <= nodes[i-1]:
                return False
        return True



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s = root  # Full tree
    t = root.left  # Subtree
    print(Solution().isValidBST(root))