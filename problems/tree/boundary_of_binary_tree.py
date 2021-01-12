"""
https://leetcode.com/problems/boundary-of-binary-tree
"""
from node_tree import TreeNode
from typing import List
class Solution:
    """
    https://www.youtube.com/watch?v=F76LIKzluKE

    Split into three parts:
    1. dfs/pre-order traversal leftmost - append before recursion
    2. dfs/pre-order traversal leaves - append before recursion
    3. post-order traversal leaves - append after recursion

    Result consist of ccw boundaries starting from root. So [left, leaves, right]
    """
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs_left(node):
            # Closure condition - if root == null or childs are both null | We're gonna grab the final left-most via leaves
            if not node or (not node.left and not node.right):
                return
            else:
                result.append(node.val)

            if node.left:  # Prioritize left child traversals first
                dfs_left(node.left)
            elif node.right:  # In event that left child doesn't exist, but right child does, this is still a valid boundary
                dfs_left(node.right)

        def dfs_leaves(node):
            if not node:
                return

            dfs_leaves(node.left)

            if node != root and (not node.left and not node.right):
                result.append(node.val)

            dfs_leaves(node.right)

        def dfs_right(node):
            # Same closure condition
            if not node or (not node.left and not node.right):
                return

            if node.right:  # Prioritize left child traversals first
                dfs_right(node.right)
            elif node.left:  # In event that left child doesn't exist, but right child does, this is still a valid boundary
                dfs_right(node.left)

            if node or not root:
                result.append(node.val)

        if not root:
            return []

        result = [root.val]

        dfs_left(root.left)
        dfs_leaves(root)
        dfs_right(root.right)

        return result



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(10)

    print("Printing Node in level order:")
    root.print_level_order(root)

    print("\nBoundaries:")
    print(Solution().boundaryOfBinaryTree(root))
