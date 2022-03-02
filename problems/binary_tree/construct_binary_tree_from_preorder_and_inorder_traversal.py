"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from node.node_tree import TreeNode
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        https://www.youtube.com/watch?v=ihj4IQGZ2zc

        Remember, first node of preorder is going to be the root.
        The inorder tells you from the root node what makes up the left and right subtree. 
        So we attain the mid index for inorder array via preorder[0] value.

        Notice that we can slice arrays as follows: 
        preorder: root|left|right
        inorder:  left|root|right

        Ex: 
        preorder = [1,2,4,5,3,6,9,7] -> root = preorder[0] = 1
        inorder =  [4,2,5,1,6,9,3,7] -> mid = inorder.index(preorder[0]) = 3
        
        preorder = [1|2,4,5|3,6,9,7]    root|left|right
        inorder =  [4,2,5|1|6,9,3,7]    left|root|right

        With array slicing, we send a piece of preorder and inorder recursively.

        Detailed example walkthrough: 
        preorder = [1,2,4,5,3,6,9,7] -> root = preorder[0] = 1
        inorder =  [4,2,5,1,6,9,3,7] -> mid = inorder.index(preorder[0]) = 3
        1 (ROOT)
                1
            /       \
        p[2,4,5]  p[3,6,9,7]
        i[4,2,5]  i[6,9,3,7]

        1->LEFT                         1->RIGHT
        preorder[1:mid+1] = [2,4,5]     preorder[mid+1:] = [3,6,9,7]
        inorder[mid+1:] = [4,2,5]       inorder[mid+1:] = [6,9,3,7]

        1->LEFT (ROOT)
        preorder = [2,4,5] -> root = preorder[0] = 2     
        inorder = [4,2,5] -> mid = inorder.index(2) = 1

                    1
                /       \
            2       p[3,6,9,7]
            /   \     i[6,9,3,7]
        p[4]   p[5]
        i[4]   i[5]

        2->LEFT                         2->RIGHT
        preorder[1:1+1] = [4]           preorder[1+1:] = [5]
        inorder[1:] = [4]           inorder[1+1:] = [5]

        2->LEFT (ROOT)
        preorder = [4] -> root = 4
        inorder = [4] -> mid = 0

                    1
                /       \
            2       p[3,6,9,7]
            /   \     i[6,9,3,7]
          4    p[5]
        /  \   i[5]
        x  x 

        preorder[0:1] = []
        inorder[0:] = []
        if not preorder or not inorder, return None

        1->RIGHT
        preorder = [3,6,9,7]
        inorder = [6,9,3,7]

        you get the idea from here.
        """
        # print(preorder, inorder)
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # preorder = [3,9,20,15,7] -> mid = 1
        # left = 1-1    right = 2->4 
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root

    def buildTreeIterative(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!
        https://jamboard.google.com/d/19j1pvZjKI2gQOi_DhS9EQK35ITF-JxsP62r1STZo3Tc/viewer
        
        Inorder gives us information on what is on the left and right at any given node.
        By definition, the number is in between left and right subtrees.
        """
        # construct hashmap mapping a value to its inorder index
        in_val_to_index = {}
        for i, val in enumerate(inorder):
            in_val_to_index[val] = i

        # Initialize stack
        root = TreeNode(preorder[0])
        stack = [root]

        # Iterate over preorder and construct the binary_tree
        for i in range(1, len(preorder)):
            # Set current node, prev to None
            curr = TreeNode(preorder[i])
            parent = None
            # print(i, curr.val, in_val_to_index[preorder[i]], in_val_to_index[stack[-1].val], stack)

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