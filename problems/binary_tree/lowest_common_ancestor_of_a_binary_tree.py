"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given constraints:
1. All nodes have unique values
2. p.val != q.val
3. p and q both exist in Tree
"""
from node.node_tree import TreeNode
class Solution:
    """
    This solution works for Binary and Binary Search Trees.

    Time and Space O(N)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return False
            
            currentCheck = root == p or root == q

            leftCheck = dfs(root.left)
            rightCheck = dfs(root.right)
                            
            if leftCheck + rightCheck + currentCheck >= 2:
                self.result = root
            if leftCheck or rightCheck or currentCheck:
                return True
            
            return False
        
        if root == p or root == q:
            return root
        
        self.result = None
        dfs(root)
        return self.result

    """
    This solution only works for binary search tree.

    https://jamboard.google.com/d/1EGspHSFDs5WNZ8JFHbgqk78TOWo6SvlWPzBsCUa6WT8/viewer
    """
    def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left.left = TreeNode(1)
    q = root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(0)

    print("Inorder print - ascending order verifies BST:")
    root.print_in_order(root)

    res = Solution().lowestCommonAncestor(root, p, q)
    print("\nResult common ancestor value: {}".format(res.val))