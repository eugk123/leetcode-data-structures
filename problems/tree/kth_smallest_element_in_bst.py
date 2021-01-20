"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
from node_tree import TreeNode
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Use Inorder to traverse through tree. Take the min everytime and end after finishing traversal. Return min
        def dfs_in_order(root):
            if root == None:
                return
            dfs_in_order(root.left)
            values.append(root.val)
            dfs_in_order(root.right)

        values = []
        dfs_in_order(root)
        return values[k-1]


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(0)
    print(Solution().kthSmallest(root, k=2))
