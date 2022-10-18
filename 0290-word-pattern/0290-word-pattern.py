class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        ptow = {}
        wtop = {}
        
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        for l, w in zip(pattern, words):
            
            if l in ptow and ptow[l] != w:
                return False
                
            if w in wtop and wtop[w] != l:
                return False
            
            if l not in ptow:
                ptow[l] = w
            
            if w not in wtop:
                wtop[w] = l
        
        return True
            