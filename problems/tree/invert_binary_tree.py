"""
https://leetcode.com/problems/invert-binary-tree
"""
from nodes.tree_node import TreeNode
import collections
class Solution:
    def invertTree(self, root):  # Recursive
        """
        https://leetcode.com/problems/invert-binary-tree/

        :type root: TreeNode
        :rtype: root: TreeNode
        """
        def dfs(root):  # DFS/pre-order
            """
            https://leetcode.com/problems/invert-binary-tree/discuss/62705/Python-solutions-(recursively-dfs-bfs).
            """

            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    node.left, node.right = node.right, node.left
                    stack.extend([node.right, node.left])
            return root

        def bfs(root):  # BFS/level-order
            """
            https://leetcode.com/problems/invert-binary-tree/discuss/62705/Python-solutions-(recursively-dfs-bfs).
            """
            queue = collections.deque([(root)])
            while queue:
                node = queue.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)
            return root

        if not root:  # Base Case -> empty tree returns empty tree
            return

        # Can replace invertTree with dfs or bfs
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        # Swap
        root.left = right
        root.right = left
        return root



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("\nLevel Order Tree:")
    root.print_level_order(root)
    print("\nLevel Order Inverted Tree:")
    root.print_level_order(Solution().invertTree(root))
