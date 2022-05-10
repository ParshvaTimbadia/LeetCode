class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndsHere = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        parent = self.root
        for letter in word:
            
            if letter not in parent.children:
                parent.children[letter] = TrieNode()
            parent = parent.children[letter]
        parent.EndsHere = True
        

    def search(self, word: str) -> bool:
        parent = self.root
        for letter in word:
            if letter not in parent.children:
                return False
            parent = parent.children[letter]
            
        if parent.EndsHere:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        
        parent = self.root
        for letter in prefix:
            if letter not in parent.children:
                return False
            parent = parent.children[letter]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)