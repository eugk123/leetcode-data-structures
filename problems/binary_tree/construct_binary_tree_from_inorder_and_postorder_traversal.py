"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""
from node.node_tree import TreeNode
from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Given:
        post  = [4,5,2,6,7,3,1]
        inord = [4,2,5,1,6,3,7]
        
        Notice in postorder traversal, when iterating from end, we can get the next root
            1 <- 1st root
        2     3 <- 2nd root
        4  5  6r   7 <- 3rd root

        Detailed walkthrough:
        dfs(0,6)
        root_value = 1 -> mid_index = 3
        in = [4,5,2,6,7,3,1]
                L  |M|  R
            l  m-1 m+1  r
            
        >>dfs(0,6).right = dfs(3+1,6)=dfs(4,6)
            root_value = 3 -> mid_index = 5
            in = [4,5,2,6,7,3,1]
                        l|M|r
            >>dfs(4,6).right = dfs(4,4)
                root_value = 7 -> mid_index = 4
                in = [4,5,2,6,7,3,1]
                            x <- l=r=m
            >>dfs(4,6).left = dfs(6,6)
                root_value = 1 -> mid_index = 6
                in = [4,5,2,6,7,3,1]
                                x <- l=r=m
        >>dfs(0,6).left = dfs(1,3-1)=dfs(0,2)
            in = [4,5,2,6,7,3,1]
                l|M|r
            root = 5 -> mid = 2
        """
        def dfs(left, right):
            # if there is no elements to construct subtrees
            if left > right:
                return None
            
            # get root value from end of postorder
            root_value = postorder.pop()
            node = TreeNode(root_value)
            
            # root splits inorder array to left | mid | right
            mid = root_val_to_inorder_index.get(root_value)
            
            # right path is from mid+1 to end
            node.right = dfs(mid + 1, right)
            
            # left path is from 0 to mid-1
            node.left = dfs(left, mid - 1)
            
            return node
    
        # We know the roots can be found from the right of the postorder array
        # We can then find the mid pointer for the inorder array.
        # So we need root_value -> inorder root_index 
        root_val_to_inorder_index = {}
        for i in range(len(inorder)):
            root_val_to_inorder_index[inorder[i]] = i
                        
        return dfs(0, len(postorder) - 1)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        See Construct Binary Tree From Preorder and Inorder Traversal.

        This is not the optimal solution because list.index(val) is O(N) which makes the entire
        time complexity of O(n^2). We are also passing deepcopies of arrays increasing the space to O(n^2) as well

        Given:
        postorder = [9,15,7,20,3] -> root = TreeNode(postorder[len(postorder)-1] = 3)
        inorder   = [9,3,15,20,7] -> mid = inorder.index(root.val) = inorder.index(3)=1


        Structure of postorder and inorder
        postorder = [9,15,7,20,3] -> |left|right|root| = |9|15,7,20|3|
                                    0:m  m:L-1   L
        inorder   = [9,3,15,20,7] -> |left|root|right| = |9|3|15,20,7|
                                    0:m   m   m+1:L
                                    
        root.left = buildTree(inorder[:mid], postorder[:mid])
        root.right = buildTree(inorder[mid+1:L-1], postorder[mid:L-1])
        """
        if not postorder or not inorder:
            return None
        L = len(postorder)
        root = TreeNode(postorder[L-1])
        mid = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:L-1])
        return root
        
    def buildTreeIterative(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        https://www.youtube.com/watch?v=s5XRtcud35E
        https://jamboard.google.com/d/19j1pvZjKI2gQOi_DhS9EQK35ITF-JxsP62r1STZo3Tc/viewer

        The core idea is: Starting from the last element of the postorder and inorder array, we put elements from postorder
        array to a stack and each one is the right child of the last one until an element in postorder array is equal to
        the element on the inorder array. Then, we pop as many as elements we can from the stack and decrease the mark
        in inorder array until the peek() element is not equal to the mark value or the stack is empty. Then, the new
        element that we are gonna scan from postorder array is the left child of the last element we have popped out from the stack.
        """
        if not inorder or not postorder:
            return None

        # Construct hashmap mapping a value to its inorder index
        in_val_to_index = {}
        for i, val in enumerate(inorder):
            in_val_to_index[val] = i

        # Root node is at the end of postorder and in stack
        root = TreeNode(postorder[len(postorder) - 1])
        stack = [root]

        # Iterate from end for postorder and construct the binary_tree
        for i in reversed(range(0, len(postorder) - 1)):
            # Set current node, prev to None
            curr = TreeNode(postorder[i])
            parent = None
            # print(i, curr.val, in_val_to_index[postorder[i]], in_val_to_index[stack[-1].val], stack)

            # We use the inorder array indices to determine whether the current node is on the left or right of parent
            # Using the parent node (in stack) and current node
            if in_val_to_index[postorder[i]] > in_val_to_index[stack[-1].val]:
                # the new node is on the right of the last node,
                # so it must be its right child (that's the way postorder works)
                stack[-1].right = curr
            else:
                # the current is on the left of the parent,
                # so it must be the left child of either the last node
                # or one of the parent's ancestors.
                # pop the stack until we either run out of ancestors
                while stack and in_val_to_index[postorder[i]] < in_val_to_index[stack[-1].val]:
                    parent = stack.pop()
                    # print(curr.val, parent.val)
                parent.left = curr
            stack.append(curr)
        return root

if __name__ == '__main__':
    tree = Solution().buildTree(postorder=[7,4,5,2,6,9,3,1], inorder=[7,4,2,5,1,6,3,9])

    print("Level-order print:")
    tree.print_level_order(tree)