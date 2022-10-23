class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Let's implement with backtracking
        wordDict = set(wordDict)
        memo = collections.defaultdict(bool)
        def helper(word):
            
            if word in wordDict:
                return True
        
            if word in memo:
                return memo[word]
            
            suffix = False
            for i in range(len(word)):
                
                sub = word[:i+1]
                
                if sub in wordDict:
                    
                    if sub == word:
                        return True
                    else:
                        suffix = helper(word[i+1:])
                        if suffix:
                            break
            
            memo[word] = suffix
            return suffix
        
        return helper(s)
                    
            