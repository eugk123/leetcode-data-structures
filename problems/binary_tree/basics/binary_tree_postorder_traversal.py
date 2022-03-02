"""
https://leetcode.com/problems/binary-tree-postorder-traversal
"""
from typing import List
from node.node_tree import TreeNode
import collections
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursive DFS is easy. Try the Iterative.
        """
        def dfs(root):
            if not root:
                return None
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            res.append(root.val)
            return

        res = []
        dfs(root)
        return res


    def postorderTraversalIterative(self, root: TreeNode) -> List[int]:
        """
        A little more complicated than DFS. Traverse far left then far right. You'll add nodes in this order:
        left -> right from bot -> top

        The easiest way to do this is to copy pre-order iterative, except you'll add left node first to stack, and add node.val to front of queue and returning the
        queue as a list.
        """
        if not root:
            return None
        res = collections.deque()

        stack = [root]
        while stack:
            curr = stack.pop()
            res.appendleft(curr.val)  # Append to front.
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return list(res)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().postorderTraversalIterative(root))