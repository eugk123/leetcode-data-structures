"""
https://leetcode.com/problems/same-tree/
"""
from node.node_tree import TreeNode
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        https://leetcode.com/problems/same-tree/

        Traverse both trees recursively. Look for conditions where False and True.

        Time complexity : O(n), where N is a number of node in the binary_tree, since one visits each node exactly once.
        Space complexity : O(log n) in the best case of completely balanced binary_tree and O(n) in the worst case of completely
        unbalanced binary_tree, to keep a recursion stack.
        """
        def dfs(p, q):
            # We know we've reached the end for both. So possibly True.
            if not p and not q:
                return True

            # Try to find all possible failure cases. That way we can continue to traverse both trees!
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val != q.val:
                return False

            if dfs(p.left, q.left) is False:
                return False
            if dfs(p.right, q.right) is False:
                return False

            # All calls have been made, so return True
            return True

        return dfs(p, q)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.left = TreeNode(4)
    q.left.right = TreeNode(5)

    print(Solution().isSameTree(p, q))
