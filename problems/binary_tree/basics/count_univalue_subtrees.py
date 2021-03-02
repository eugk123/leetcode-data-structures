"""
https://leetcode.com/problems/count-univalue-subtrees/
"""
from node_tree import TreeNode
class Solution:
    """
    This video does a great job with explaining univalue subtrees by giving tons of examples.
    https://www.youtube.com/watch?v=ML3OgQoSWTE

    The example below has total 15.
              5   +1 (entire binary_tree is univalue)
            /   \
         5         5   +2 (each bigger subtree of depth 3)
       /   \     /   \
      5    5    5    5   +4 (each subtree of depth 2)
     / \  / \  / \  / \
    5  5 5  5 5  5 5   5  +8 (all leaves)

    In order to check if bigger subtree is a univalue subtree of subtrees, each bottom subtree needs to pass parent
    a boolean stating that it's subtree is univalue.
    """
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def dfs_post_order(root):
            """
            Need to use post order because we want to traverse to the bottom children to check if the parent is indeed
            univalue with the children nodes.
            """
            # If null, return 0 count. Univalue is True.
            if not root:
                return 0, True

            # If leaf node, return 1 count. Univalue is True.
            if not root.left and not root.right:
                return 1, True  # Return +1 for count and True for univalue


            # Traverse first - Post order
            left_count, is_left_univalue = dfs_post_order(root.left)
            right_count, is_right_univalue = dfs_post_order(root.right)

            # If children are both univalued, we know that current node can potentially be univalued as well!
            # As long as the value of root is equal to the value of children.
            if is_left_univalue and is_right_univalue:

                # True Cases
                if root.left and not root.right:
                    if root.val == root.left.val:
                        return 1 + left_count + right_count, True
                elif root.right and not root.left:
                    if root.val == root.right.val:
                        return 1 + left_count + right_count, True
                elif root.left and root.right:
                    if root.val == root.left.val == root.right.val:
                        return 1 + left_count + right_count, True

            # All other cases or at end, return False and left + right.
            # Removes the need of an else statement on previous condition
            return left_count + right_count, False

        return dfs_post_order(root)[0]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    # root.left.right = TreeNode(1)
    # root.left.left.left = TreeNode(1)
    print(Solution().countUnivalSubtrees(root))
