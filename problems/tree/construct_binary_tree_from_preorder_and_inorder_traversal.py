"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from node_tree import TreeNode
from typing import List
class Solution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!
    https://jamboard.google.com/d/19j1pvZjKI2gQOi_DhS9EQK35ITF-JxsP62r1STZo3Tc/viewer
    
    Inorder gives us information on what is on the left and right at any given node.
    By definition, the number is in between left and right subtrees.
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # construct hashmap mapping a value to its inorder index
        in_val_to_index = {}
        for i, val in enumerate(inorder):
            in_val_to_index[val] = i

        # Initialize stack
        root = TreeNode(preorder[0])
        stack = [root]

        # Iterate over preorder and construct the tree
        for i in range(1, len(preorder)):
            # Set current node, prev to None
            curr = TreeNode(preorder[i])
            parent = None
            print(i, curr.val, in_val_to_index[preorder[i]], in_val_to_index[stack[-1].val], stack)

            if in_val_to_index[preorder[i]] < in_val_to_index[stack[-1].val]:
                # the new node is on the left of the last node,
                # so it must be its left child (that's the way preorder works)
                stack[-1].left = curr
            else:
                # the new node is on the right of the last node,
                # so it must be the right child of either the last node
                # or one of the last node's ancestors.
                # pop the stack until we either run out of ancestors
                # or the node at the top of the stack is to the right of the new node
                while stack and in_val_to_index[preorder[i]] > in_val_to_index[stack[-1].val]:
                    parent = stack.pop()
                parent.right = curr
            stack.append(curr)
        return root


if __name__ == '__main__':
    tree = Solution().buildTree(preorder=[1,2,4,7,5,3,6,9], inorder=[7,4,2,5,1,6,3,9])

    print("Level-order print:")
    tree.print_level_order(tree)