class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        #Bottom Up Solution:
        wordDict = set(wordDict)
        memo = {}
        def helper(sub):
            
            if sub in memo:
                return memo[sub]
            
            result = []
            
            for i in range(len(sub)):
                
                prefix = sub[:i+1]
                
                if prefix in wordDict:
                    
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        for later in helper(sub[i+1:]):
                            result.append(prefix+ " " + later)   
            
            memo[sub] = result
            return result
        
        return helper(s)
        