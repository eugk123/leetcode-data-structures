"""
https://leetcode.com/problems/word-ladder/
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """

        Best Solution IMO:
        https://leetcode.com/problems/word-ladder/discuss/1764371/A-very-highly-detailed-EXPLANATION

        Where M: # of letters, N: # of words
        Time O(M*N)
        Space O(M*N)
        """
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])  # initialize queue with first word and # of steps
        visited = set()
        while queue:  # iterate through all words -> N time
            curr, steps = queue.popleft()

            if curr == endWord:
                return steps
            
            # iterate through each letter -> M time
            for i in range(len(curr)):
                char_array = list(curr) # convert to char array - h,i,t
                for j in range(26):
                    char_array[i] = chr(ord("a") + j)   # *it, h*t, hi*
                    neighbor = "".join(char_array)
                    
                    if neighbor in visited:
                        continue

                    # ["hot","dot","dog","lot","log","cog"]
                    if neighbor in wordSet:  # h*t -> hot
                        queue.append((neighbor, steps + 1))
                        visited.add(neighbor)
                        
        return 0

    def ladderLengthTLE(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Build Graph then perform BFS. TLE because this is an N^2 solution.

        Where M: # of letters, N: # of words
        Time O(M * N^2)
        """
        def isOneEditAway(node1: Node, node2: Node):
            word1 = node1.word
            word2 = node2.word
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            
                if count > 1:
                    return False
            return True
        
        def buildGraph(beginWord: str, wordList: List[str]):
            
            # Need map to track word -> node
            word_to_node = {}
            
            # Add first word to list
            wordList.append(beginWord)
            
            # Use two pointers to connect all possible combinations. We iterate j pointer with i+1 to avoid duplicate connections.
            for i in range(len(wordList)):
                for j in range(i + 1, len(wordList)):
                    if wordList[i] in word_to_node:
                        prev = word_to_node[wordList[i]]
                    else:
                        prev = Node(wordList[i])
                        word_to_node[wordList[i]] = prev

                    if wordList[j] in word_to_node:
                        curr = word_to_node[wordList[j]]
                    else:
                        curr = Node(wordList[j])
                        word_to_node[wordList[j]] = curr

                    if isOneEditAway(prev, curr):
                        prev.neighbors.append(curr)
                        curr.neighbors.append(prev)
                    
                    
            return word_to_node
        
        def bfs(beginWord, endWord, word_to_node):
            source = word_to_node[beginWord]
            queue = deque([(source, 1)])  # initialize queue
            visited = set()
            visited.add(source)
            
            while queue:
                curr, steps = queue.popleft()
                for nei in curr.neighbors:
                    if nei.word == endWord:
                        return steps + 1

                    if nei in visited:
                        continue
                        
                    visited.add(nei)
                    
                    queue.append((nei, steps + 1))
            
            return 0
        
        word_to_node = buildGraph(beginWord, wordList)

        if not word_to_node.get(endWord):
            return 0
        
        return bfs(beginWord, endWord, word_to_node)

class Node:
    def __init__(self, word):
        self.word = word
        self.neighbors = []
