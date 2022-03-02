"""
https://leetcode.com/problems/binary-tree-paths
"""
from node.node_tree import TreeNode
class Solution:
    """
    Time & Space O(N)

    Using a string builder or a char array would be more optimal for time
    https://leetcode.com/problems/binary-tree-paths/discuss/760438/Time-Complexity-Analysis-String-vs-StringBuilder

    
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        def dfs(root, path):
            # when leaf node is hit, add to result
            if not root.left and not root.right:
                result.append(path)
            
            #
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
            
        result = []
        dfs(root, str(root.val))
        return result