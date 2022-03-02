"""
https://leetcode.com/problems/maximum-depth-of-binary-tree
"""
from node.node_tree import TreeNode
from collections import deque
class Solution:
    def maxDepth(self, root):
        def dfs(root, depth):
            self.maxDepth = max(self.maxDepth, depth)
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)

        if root is None:
            return 0
        self.maxDepth = 1
        dfs(root, 1)

        return self.maxDepth

    def maxDepthIterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case, returning depth of 0 when root is empty
        if root is None:
            return 0

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().maxDepth(root))
