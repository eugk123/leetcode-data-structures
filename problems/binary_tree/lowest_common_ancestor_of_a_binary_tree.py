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
    def lowestCommonAncestorEugene(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        This solution works for Binary and Binary Search Trees.
        
        When node == p or node == q, we update global result = node.
        When left and right are both True, we update global result = node.

           1       left == True, right == True
         T/ \T     result = 1
        p2   3q
        
           1       left = True @ 2, right = False
         T/ \F     result = 2
        p2   3
          \
          q4 
        Time and Space O(N)
        """
        def dfs(root):
            # null, return False
            if not root:
                return False
            
            # found p or q, return True, update result
            if root == p or root = q:
                self.result = root
                return True

            left = dfs(root.left)
            right = dfs(root.right)

            # in the event that p and q are on opposite sides of the root, 
            # we can overwrite current result with the true LCA.
            if left and right:
                self.result = root

            # we want to make sure we are returning True if one of the sides has p or q.
            # this is required for finding the LCA if two nodes are on different ends of the root.
            if left and not right:
                return True
            if not left and right:
                return True
                
            return False
        
        self.result = None
        dfs(root)
        return self.result
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        This solution works for Binary and Binary Search Trees.

        Time and Space O(N)
        """
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