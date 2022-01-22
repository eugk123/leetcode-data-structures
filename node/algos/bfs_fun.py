import collections

class BFS:
    def __init__(self, input, condition:int=0):
        self.input = input
        self.condition = condition

        # Condition 0 - count when value == 0
        # Condition 1 - calculate shortest path to valid gates (value = 1)
        
        BFS.matrix(input, {}, condition)

        # if self.input is type matrix:
        #     BFS.matrix(input)
        # elif self.input is type TreeNode:
        #     BFS.tree(input)
        # elif self.input is type GraphNode:
        #     BFS.graph(input)
        # else:
        #     print("Please use an input type of one of the following:")
        #     print("(1): Matrix")
        #     print("(2): Tree")
        #     print("(3): Graph")

    def matrix(input, visited, condition):
        print("Running BFS Matrix Example using input: {}".format(input))

        def bfs(i, j, condition):
            current = queue.popleft()
            c_i = current[0]
            c_j = current[1]

            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for direction in directions:
                i = c_i + direction[0]
                j = c_j + direction[1]

            count = 0
            if condition == 0:
                print("CONDITION 0: Count number of nodes with value equal to 0")

        # Initialize empty queue
        queue = collections.deque([])

        # Iterate through all possible indices to ensure are reached
        for i in range(len(input)):
            for j in range(len(input)):
                bfs(i,j,condition)




    def tree():
        print("Running BFS Tree Example")
        return

    def graph():
        print("Running BFS Graph Example")
        return

if __name__ == '__main__':
    input = [[1,0,0],[1,1,0],[1,0,1],[1,0,0]]