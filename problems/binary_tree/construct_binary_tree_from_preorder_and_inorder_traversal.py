"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from node.node_tree import TreeNode
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - We understand that preorder traversal is print -> dfs(left) -> dfs(right), therefore, we know that
          we can create the node and set left and right pointers from left to right of the preorder array.
          This will require a global variable self.preorder_index and each iteration prior to going deeper, we traverse += 1
        - If we know the root value, we can split the inorder to left and right subtrees

        -> root = preorder[0] = 1
        -> mid = inorder.index(preorder[0]) = 3
                    R
        preorder = [1,2,4,5,3,6,9,7]    
        inorder =  [4,2,5|1|6,9,3,7]    left|root|right     so left = [4,2,5] and right = [6,9,3,7]
                    |   | m |     |                                   0--- m-1           m+1 ----- L
                    l   r   l     r   we can set left and right indices for LEFT and RIGHT paths

        - We first need a hashmap containing num -> index for inorder. 
        - In our dfs method, we should be iterating through each preorder value in the array prior to going deeper
        - We get the inorder root index and we can update the left and right indexes for the left and right path
        - For left path, left index is always set to 0 and right index is always set to mid - 1
        - For right path, right index is always set to mid + 1 and right index is always set to end (length - 1)
        - Eventually, l and r pointers will pass each other when the leafnode get's attached. So we return on left > right
        - At the end of the method, we want to return the root.

        """
        find_inorder_mid = {}
        
        for i in range(len(inorder)):
            find_inorder_mid[inorder[i]] = i
        
        def dfs(left, right):
            # left and right pointers
            if left > right:
                return
            
            # assign root value, initially should be index 0 of preorder
            root_value = preorder[self.preorder_index]
            
            # create Node using root value
            node = TreeNode(root_value)
            
            # update mid index from inorder array
            mid = find_inorder_mid.get(root_value)

            # similar to printing preorder values, we can traverse to the right
            self.preorder_index += 1  
            
            # left side of tree of the inorder is between beginning(0) and mid-1
            node.left = dfs(left, mid - 1)
            
            # right side of tree of the inorder is between mid+1 and end(L-1)
            node.right = dfs(mid + 1, right)
        
            return node
        
        self.preorder_index = 0
        return dfs(0, len(inorder) - 1)
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        https://www.youtube.com/watch?v=ihj4IQGZ2zc

        This is not the optimal solution because list.index(val) is O(N) which makes the entire
        time complexity of O(n^2). We are also passing deepcopies of arrays increasing the space to O(n^2) as well

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