"""
https://leetcode.com/problems/complete-binary-tree-inserter/
"""
from node_tree import TreeNode
class CBTInserter:
    """
    https://www.youtube.com/watch?v=GaF-UdKklRQ

    A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
    and all nodes are as far left as possible.

    Valid CBT   Invalid CBT
        1           1
       / \         / \
      2  3        2   3
     / \         /   /
    4  5        4   6
    """
    def __init__(self, root: TreeNode):
        """
        initializes the data structure on a given tree with head node root
        """

        self.root = root
        self.parentNodeFound = False  # This is used to simply find the first parent node.

        # Initialize an "insert" queue which will capture any existing and newly added leaf nodes.
        self.insertQueue = []

        # Perform typical BFS using queue
        queue = [self.root]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)

                # Here you'll store the parent node which will have an inserted node
                if not self.parentNodeFound and (not curr.left or not curr.right):
                    self.parentNodeFound = True
                    self.parentNode = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                # Here you'll capture all remaining leaf nodes and add to initialized "insert" queue
                if self.parentNodeFound:
                    self.insertQueue.append(curr)



    def insert(self, v: int) -> int:
        """
        will insert a TreeNode into the tree with value node.val = v so that the tree remains complete,
        and returns the value of the parent of the inserted TreeNode;

        To satify CBT conditions, insertion must occur at last level if unfilled on far left, or new level far left.
            1            1                          1         1
           / \          / \                        /         / \
          2   3        2   3                     2          2   3  INSERTED LAST LEVEL FAR LEFT
                      /
                     4 INSERTED NEW LEVEL FAR LEFT
        """
        # Check if left is vacant.
        if not self.parentNode.left:
            self.parentNode.left = TreeNode(v)
            self.insertQueue.append(self.parentNode.left)   # Insert into Queue to allow for additional processing of future inserted nodes
            return self.parentNode.val

        # Check if right is vacant.
        elif not self.parentNode.right:
            self.parentNode.right = TreeNode(v)
            self.insertQueue.append(self.parentNode.right)   # Insert into Queue to allow for additional processing of future inserted nodes
            return self.parentNode.val

        # In the event that both children are not vacant, pull next node from insertQueue, set as parent and recursively run insertion.
        else:
            self.parentNode = self.insertQueue.pop(0)
            return self.insert(v)

    def get_root(self) -> TreeNode:
        """
        Return head node of the tree
        """
        return self.root.val



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    obj = CBTInserter(root)
    param_1 = obj.insert(5)
    obj.insert(6)
    obj.insert(6)
    obj.insert(6)
    obj.insert(6)
    obj.insert(6)
    param_2 = obj.get_root()

    print("BFS Print of root:")
    root.print_level_order(root)

    print("\nParent Value of Inserted Node: {}".format(param_1))
    print("Root Node Value: {}".format(param_2))

