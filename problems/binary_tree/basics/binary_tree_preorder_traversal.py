"""
https://leetcode.com/problems/binary-tree-preorder-traversal
"""
from typing import List
from node_tree import TreeNode
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursive DFS is easy. Try the Iterative.
        """
        def dfs(root):
            if not root:
                return None
            res.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return

        res = []
        dfs(root)
        return res

    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        """
        For Iterative, know when to push and pop in the stack. When you pop, that's your only chance to write to list.

        Preorder traversal is DFS in which you go from root -> left -> right. You can add result as soon as you pop.
        Then add the right node first to the stack. Then add the left.
        """
        if not root:
            return None
        res = []

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().preorderTraversalIterative(root))