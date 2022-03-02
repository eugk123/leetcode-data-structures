"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
from node.node_tree import TreeNode
class Solution:
    def kthSmallestDfsRecursive(self, root: TreeNode, k: int) -> int:
        # Use Inorder to traverse through binary_tree. Take the min everytime and end after finishing traversal. Return min
        def dfs_in_order(node):
            if not node:
                return

            dfs_in_order(node.left)
            res.append(node.val)
            dfs_in_order(node.right)

        res = []
        dfs_in_order(root)
        return res[k - 1]

    # def kthSmallestDfsIterative(self, root: TreeNode, k: int) -> int:

        # stack = [root]
        # values = []
        # while stack:
        #
        #     curr = stack.pop()
        #     values.append(curr.val)
        #
        #     if curr.right:
        #         stack.append(curr.left)
        #     if curr.left:
        #         stack.append(curr.right)

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(0)
    print(Solution().kthSmallestDfsRecursive(root, k=2))
