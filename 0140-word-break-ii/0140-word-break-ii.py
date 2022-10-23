class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # Let's implement with backtracking
        wordDict = set(wordDict)
        memo = collections.defaultdict(bool)
        def helper(word):
            
            if word in memo:
                return memo[word]
            
            result = []
            for i in range(len(word)):
                
                sub = word[:i+1]
                
                if sub in wordDict:
                    
                    if sub == word:
                        result.append(word)
                    else:
                        for w in helper(word[i+1:]):
                            result.append(sub+" "+w)
                            
            memo[word] = result
            return result
        
        return helper(s)
        