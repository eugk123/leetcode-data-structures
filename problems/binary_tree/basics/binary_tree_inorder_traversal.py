"""
https://leetcode.com/problems/binary-tree-inorder-traversal
"""
from typing import List
from node_tree import TreeNode
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursive DFS is easy. Try the Iterative.
        """
        def dfs_in_order(root):
            if not root:
                return

            if root.left:
                dfs_in_order(root.left)

            res.append(root.val)

            if root.right:
                dfs_in_order(root.right)

        res = []
        dfs_in_order(root)
        return res

    def inorderTraversalIterative_MySolution(self, root: TreeNode) -> List[int]:
        """
        For Iterative, know when to push and pop in the stack. When you pop, that's your only chance to write to list.

        Inorder traversal is an ascending BST. You first hit the bottom leftmost node, to the parent, to the right
        Therefore, right of the bat, you need to push to stack until you get as far left as possible.
        Then you need to pop when null and pop again until you can push right
        """
        if root is None:
            return None

        stack = [root]
        curr = root
        res = []
        while stack:
            while curr.left:
                stack.append(curr.left)
                curr = curr.left

            # Pop leftmost node, this will hit again popping the parent since curr.left is still empty
            curr = stack.pop()
            curr.left = None

            res.append(curr.val)

            # Now traverse right once. Then repeat!
            if curr.right:
                stack.append(curr.right)
                curr = curr.right
        return res


    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        """
        This is the most optimal. My solution forces curr.left to point to None so it doesn't traverse left again.

        In this solution, you're always traversing to the right even when empty. When curr.right is empty, then the
        while curr: loop is skipped allowing you to continuously move up popping elements from stack.
        """
        if root is None:
            return None

        res, stack = [], []
        curr = root

        # While curr is needed because stack will be empty and this loop needs to keep going.
        # This solution is very difficult to come up with from scratch.
        while curr or stack:

            # Travel to each node's left child, till reach the left leaf
            # Notice we're using curr instead of curr.left. This is because we expect curr -> None
            # When curr -> None, curr.left will error out.
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()  # this node has no left child
            res.append(curr.val)  # so let's append the node value

            # Visit its right child --> Here if right exists, then we repeat the entire process again and move to the
            # left most node in the next interation. If right is None, then this loop allows us to move up by skipping
            # the while curr: and popping the next element.
            curr = curr.right
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().inorderTraversalIterative(root))