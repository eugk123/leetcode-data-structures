"""
https://leetcode.com/problems/invert-binary-tree
"""
from node_tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # This has to be post order because the swaps must occur leaves first

        def dfs_post_order(root):
            # Recursive post order traversal
            if root.left:
                dfs_post_order(root.left)
            if root.right:
                dfs_post_order(root.right)

            # Swap nodes
            temp_left = root.left
            temp_right = root.right
            root.left = temp_right
            root.right = temp_left

        # Base case
        if not root:
            return root

        dfs_post_order(root)
        return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("\nLevel Order Tree:")
    root.print_level_order(root)
    print("\nLevel Order Inverted Tree:")
    root.print_level_order(Solution().invertTree(root))
