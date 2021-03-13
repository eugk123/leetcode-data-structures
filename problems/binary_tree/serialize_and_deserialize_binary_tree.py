"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
from node_tree import TreeNode
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Base Case - empty
        if not root:
            return root

        # BST and use markers to tell what level we're at
        # Mark L and R as well for null and also use ',' to separate every element
        # Use '|' to tell you we're at the next level
        queue = deque([root])
        tree_string = []

        # Add root to string
        tree_string.append(str(root.val))
        tree_string.append(",")

        while queue:
            # Indicate next level on string
            for _ in range(len(queue)):
                curr = queue.popleft()

                # Make sure to include left and right null indicators.
                # Order matters here.
                if curr.left:
                    queue.append(curr.left)
                    tree_string.append(str(curr.left.val))
                    tree_string.append(",")
                if not curr.left:
                    tree_string.append("N")
                    tree_string.append(",")
                if curr.right:
                    queue.append(curr.right)
                    tree_string.append(str(curr.right.val))
                    tree_string.append(",")
                if not curr.right:
                    tree_string.append("N")
                    tree_string.append(",")
        return "".join(tree_string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Base Case - empty
        if not data:
            return data

        # Convert string to an array with the commas removed!
        data = list(data.split(','))
        data.pop()  # Removes extra empty string

        # You can perform BFS again to build the tree with all the existing nodes in the list.
        queue = deque([])
        root = TreeNode(int(data[0]))
        queue.append(root)

        # Analyzing the conversion of level-order collection of element values,
        # We see the conversion is as follows for index i:
        # current    left     right
        #    i     = 2*i + 1, 2*i + 2
        i = 0
        while queue:
            curr = queue.popleft()

            if data[2 * i + 1] != 'N':
                curr.left = TreeNode(int(data[2 * i + 1]))
            if data[2 * i + 2] != 'N':
                curr.right = TreeNode(int(data[2 * i + 2]))

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    string = Codec().serialize(root)
    print("Serialized binary_tree to string:")
    print(string)
    new_root = Codec().deserialize(string)
    print("\nDeserialized String to Tree, Level Order Print:")
    root.print_level_order(new_root)