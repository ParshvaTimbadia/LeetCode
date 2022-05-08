class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endsHere = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        char = self.root
        for letter in word:
            if letter not in char.children:
                char.children[letter] = TrieNode()
            char = char.children[letter]
        
        char.endsHere = True

    def search(self, word: str) -> bool:
        
        def helper(index, char):
            
            if index == len(word):
                if char.endsHere:
                    return True
                return False
            
            if word[index] in char.children:
                return helper(index+1, char.children[word[index]])
            
            elif word[index] == ".":
                for letter in char.children.keys():
                    if helper(index+1, char.children[letter]):
                        return True
            
            return False
            
        
        return helper(0, self.root)
                    
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)