"""
This is the iterative implementation of DFS.
"""
from node.node_tree import TreeNode
def dfs(root: TreeNode):

   stack = [root]  # Initialize stack with root
   while stack:
       curr = stack.pop()

       # do something here
       print(curr.val)  # Replace print.

       if curr.right:  # append opposite direction
           stack.append(curr.right)
       if curr.left:  # append first direction afterwards
           stack.append(curr.left)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    dfs(root)
