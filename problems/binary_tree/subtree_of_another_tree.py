"""
https://leetcode.com/problems/subtree-of-another-tree/
"""
from node.node_tree import TreeNode
class Solution:
    """
    Use PreOrder (DFS) traversal
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        # DFS function contains input TreeNode and boolean isLeft
        def dfs(t, isLeft):
            # If t is null, we'll be grabbing lnull or rnull depending on left or right
            if t is None:
                if isLeft is True:
                    return "lnull"
                else:
                    return "rnull"

            # Update current value. Use # to avoid success from different trees with multiple digits.
            # For ex: 23 and 3 t.val.
            tree_string = "#" + "{}".format(t.val)

            # Recursively call for left and right children nodes
            tree_string += " " + dfs(t.left, True)
            tree_string += " " + dfs(t.right, False)

            return tree_string

        tree1 = dfs(s, True)
        tree2 = dfs(t, True)
        print(tree1)
        print(tree2)

        # tree1.index(tree2) will fail if tree1 is not a substring of tree2
        try:
            # If it is a substring, then return True
            if tree1.index(tree2) >= 0:
                return True
        except:
            return False


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(4)

    s = root  # Full binary_tree
    t = root.left  # Subtree
    print(Solution().isSubtree(s, t))