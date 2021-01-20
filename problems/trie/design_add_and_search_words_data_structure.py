from node_trie import TrieNode
class WordDictionary:
    """
    https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/774530/Python-Trie-solution-with-dfs-explained

    Approach using DFS
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds word to the data structure, it can be matched later.
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word or false otherwise.

        word may contain dots '.' where dots can be matched with any letter
        """
        def dfs(node, i):
            # 1. Check necessary conditions
            if i == len(word):
                return node.isWord

            # 3. Call DFS as needed
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i + 1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)

            return False

        return dfs(self.root, 0)


if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord(word="try")
    print(obj.search(word="..y"))