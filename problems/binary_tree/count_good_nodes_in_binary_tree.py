"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree
"""
from node.node_tree import TreeNode
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            # If empty, return
            if not node:
                return

            # If max is found, add to count
            if node.val >= current_max:
                self.count += 1

            # Update max
            current_max = max(current_max, node.val)

            # Traverse left then right
            if node.left:
                dfs(node.left, current_max)

            if node.right:
                dfs(node.right, current_max)

            return

        self.count = 0
        current_max = -math.inf
        dfs(root, current_max)
        return self.count