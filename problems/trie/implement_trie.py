"""
https://leetcode.com/problems/implement-trie-prefix-tree/solution/
"""
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return True

if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    obj = Trie()
    obj.insert(word="hello")
    print(obj.search(word="hello"))
    print(obj.startsWith(prefix="hell"))
    print(obj.startsWith(prefix="llo"))