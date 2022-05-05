class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endsHere = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        path = self.root
        for letter in word:
            if letter not in path.children:
                path.children[letter] = TrieNode()
            path = path.children[letter]
        path.endsHere = True
        

    def search(self, word: str) -> bool:
        
        path = self.root
        for letter in word:
            if letter not in path.children:
                return False
            path = path.children[letter]
        
        if path.endsHere == True:
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        
        path = self.root
        for letter in prefix:
            if letter not in path.children:
                return False
            path = path.children[letter]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)