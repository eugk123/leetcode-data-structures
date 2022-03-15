"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Preorder DFS w/ linear list iteration.

        Time and Space O(N)
        """
        
        def dfs(root, prev):
            # update previous & do a preorder add to list
            prev = root
            ordered.append(root)

            # traverse and detach node to prevent cycles
            if root.left:
                dfs(root.left, prev)
            prev.left = None
            
            if root.right:
                dfs(root.right, prev)
            prev.right = None
        
        # edge case - empty
        if not root:
            return None

        # initialize list and run dfs
        ordered = []
        dfs(root, None)
        
        # set head pointer
        head = prev = ordered[0]
        
        # iterate through list and attach using prev pointer
        for curr in ordered[1:]:
            if prev:
                prev.right = curr
            prev = curr
        return head