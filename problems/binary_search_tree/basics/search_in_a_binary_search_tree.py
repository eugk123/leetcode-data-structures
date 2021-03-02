"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""
from node_tree import TreeNode
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        This effectively searches the entire binary_tree which is not an optimized solution. But same time as worst case O(N).
        """
        def dfs(node):
            if not node:
                return
            if node.val == val:
                self.ans = node
                return

            dfs(node.left)
            dfs(node.right)

        self.ans = None
        dfs(root)
        return self.ans

    def searchBSTOptimized(self, root: TreeNode, val: int) -> TreeNode:
        """
        More optimized solution would be to leverage the BST property when traversing.

        Since values go from left < parent < right, we know we can traverse towards the correct direction based on current value.
        Thus saving time.

        However, for a straight line binary_tree, the worst time complexity would still be O(N)
        """
        def dfs(node):
            if not node:
                return node
            if node.val == val:
                return node

            if node.val > val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)
