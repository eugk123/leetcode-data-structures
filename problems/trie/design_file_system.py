class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        """
        Creates a new path and associates a value to it if possible and returns true. Returns
        false if the path already exists or its parent path doesn't exist.
        
        Time O(N), Space O(N)
        """
        # /leet/code
        # check if /leet exists
        paths = path.split("/")
        curr = self.root
        
        if len(paths) <= 1:
            return False
        
        for i in range(1, len(paths)):
            path = paths[i]
            # First check if we're at the end. If we're not at the end, and we cannot find the path, we know this cannot be added
            if i < len(paths) - 1:
                if path not in curr.children:
                    return False
                else:
                    curr = curr.children[path]
                    
            # If we at the end, /leet/code, suppose we at /code, we should expect /code not to be there. If it is, then return False
            else:
                if path not in curr.children:
                    curr.children[path] = TrieNode()
                    curr.children[path].value = value
                    return True

        return False

    def get(self, path: str) -> int:
        """
        Returns the value associated with path or returns -1 if the path doesn't exist.        
        """
        paths = path.split("/")
        curr = self.root
        # print(paths)
        # print(curr.children)
        
        for path in paths[1:]:
            if path in curr.children:
                curr = curr.children[path]
            else:
                return -1

        return curr.value