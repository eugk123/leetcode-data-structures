"""
https://leetcode.com/problems/same-tree/
"""
from node_tree import TreeNode
class Solution:
    def isSameTree(self, p, q):  # Recursion
        """
        https://leetcode.com/problems/same-tree/

        When using Recursion, you want to make sure your conditions do stop your algorithm from reaching all the node.
        Therefore, cases such as the following will cause the algo to end early:
            - p.val == q.val -> True
            - if p and q -> True
        Instead, you want to find the opposite conditions and find one final true statement. This final true statement,
        is critical:
            - if not p and not q (if p and q are both None)

        Time complexity : O(n), where N is a number of node in the tree, since one visits each node exactly once.
        Space complexity : O(log n) in the best case of completely balanced tree and O(n) in the worst case of completely
        unbalanced tree, to keep a recursion stack.

        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:  # If you try using p.val == q.val, this will not work recursively. It will end immediately.
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

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
