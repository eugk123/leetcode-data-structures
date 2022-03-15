class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.sentence = None
        self.rank = 0
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        """
        sentences = ["i love you", "island", "iroman", "i love leetcode"]
        times     = [5, 3, 2, 2]
        
        - What's the most optimal data structure to store words for prefix word retrieval?        
        - We can store all sentences in a Trie data structure which is optimized to get all words with prefix.
        
        - What can we do with determining hotness? 
        - Trie data structure will also have self.rank that is used for getting the rank for a particular word and self.sentence that is used for returning the full sentence for prefixWordSearch
        - We can store all returned sentences based on prefix and iterate through them again to store in a priority queue 
        - When getting words starting with prefix, make sure to store matched words with (-rank, word)
        """
        self.prefix = ""  # used for getting all words starting with this prefix
        self.trie = TrieNode()
        self.prefix_words = []
        
        # build Trie
        for i in range(len(times)):
            # insert sentence and rank
            self.insertSentence(sentences[i], times[i])
            
    def insertSentence(self, sentence: str, rank: int):
        # Iterate letter by letter and add to Trie
        current = self.trie
        for i in range(len(sentence)):
            # insert letter by letter
            letter = sentence[i]
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]

        # at end, we want to set that we completed the word and also the hotness
        current.is_word = True
        
        # if rank = 0, this indicates an insertion from user.
        # increment existing time by 1; if new, set to 1
        
        if current.rank:
            current.rank += 1
        elif not current.rank and rank == 0:
            current.rank = 1
        else:
            current.rank = rank
        current.sentence = sentence

        
    def getSentencesStartingWithPrefix(self, prefix: str) -> List[str]:
        current = self.trie
        
        def dfs(current):
            # end of each trie will be a word; append that word when end is reached
            if current.is_word:
                # append in tuple to allow for heap sorting
                # we need to use a max heap to get top K sentences; therefore -current.times is used
                results.append((-current.rank, current.sentence))  
            
            # explore paths starting with next word
            for letter in current.children:
                dfs(current.children[letter])
        
        # traverse to word prefix on trie first.
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return []
            
        # then get all words
        results = []
        dfs(current)
        return results
    
    def input(self, c: str) -> List[str]:
        """
        "i"   -> ["i love you", "island", "i love leetcode"]   ordered by highest times and then ordered by lowest ASCII value
        "i "  -> ["i love you", "i love leetcode"]
        "i a" -> []
        "i a#"-> [] user finished input
        Constructor will have a global parameter that stores current prefix. This prefix is updated with the input.
        
        returns top 3 in a list
        """
        # Update prefix used for getting all words starting with prefix string
        # If input is a hashtag '#', add to Trie and return []
        # We use a 0 input, because this indicates we're simply incrementing the times if it already exists. See insert method.
        if c == "#":
            self.insertSentence(self.prefix, 0)
            self.prefix = ""
            return []
        else:
            self.prefix = self.prefix + c
                
        # Matched sentences are tuples with each element as (-times, sentence)
        matched_sentences = self.getSentencesStartingWithPrefix(self.prefix)

        # Convert to heap (max heap)
        heapq.heapify(matched_sentences)
        
        # Append top three sentences
        top_results = []
        
        # If there are less than 3 matches, update count
        if len(matched_sentences) < 3:
            result_count = len(matched_sentences)
        else:
            result_count = 3
        
        # Get top results via popping from heap
        for i in range(result_count):
            top_sentence = heapq.heappop(matched_sentences)[1]
            top_results.append(top_sentence)
            
        return top_results

        
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)