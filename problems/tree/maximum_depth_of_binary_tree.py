from node_tree import TreeNode
import collections
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur_root = queue.pop(0)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth

    def maxDepth_deque(self, root):
        """
        https://leetcode.com/problems/maximum-depth-of-binary-tree/

        The BFS algorithm works great here.
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tqueue, h = collections.deque(), 0
        tqueue.append(root)
        while tqueue:
            nextlevel = collections.deque()
            while tqueue:
                front = tqueue.popleft()
                if front.left:
                    nextlevel.append(front.left)
                if front.right:
                    nextlevel.append(front.right)
            tqueue = nextlevel
            h += 1
        return h

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().maxDepth(root))
