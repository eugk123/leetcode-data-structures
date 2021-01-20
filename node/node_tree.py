class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_level_order(self, arr, root, i, n):
        # Base case for recursion
        if i < n:
            temp = TreeNode(arr[i])
            root = temp

            # insert left child
            root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root

    def print_in_order(self, root):
        if root:
            self.print_in_order(root.left)
            print(root.val, end=" ")
            self.print_in_order(root.right)

    def print_pre_order(self, root):
        if root:
            print(root.val, end=" ")
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_post_order(self, root):
        if root:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.val, end=" ")

    def print_level_order(self, root):
        # Base Case: empty root -> depth = 0
        # level is set to be a queue
        if root:
            level = [root]
        else:
            level = []

        while level:
            queue = []  # Start with Empty Queue

            for curr in level:  # Add children node for element
                # Do something
                print(curr.val, end=" ")

                # Populate Queue with Children TreeNodes
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # The level Array will keep growing from [2 3] to [4 5 6 7] to 8 items to 16 and so forth
            level = queue
#
# # Driver Code
# if __name__ == '__main__':
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#
#     print("\nPrinting Pre Order:")
#     pre_order(root)
#     print("\nPrinting In Order:")
#     in_order(root)
#     print("\nPrinting Post Order:")
#     post_order(root)
#     print("\nPrinting Level Order:")
#     level_order(root)
#
#     # Insert Level Order via Array
#     arr = [1, 2, 3, 4, 5]
#     new_root = None
#     new_root = insert_level_order(arr, new_root, 1, len(arr))
#
#     print("\nPrinting In Order (Array Insertion):")
#     in_order(new_root)


