class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        wordDict = set(wordDict)
        result = []
        
        def helper(index, slate):
            
            if index == len(s):
                result.append(" ".join(slate[:]))
                return
            
            for i in range(index, len(s)):
                
                subArray = s[index:i+1]
                
                if subArray in wordDict:
                    
                    slate.append(subArray)
                    helper(i+1, slate)
                    slate.pop()
        
        
        helper(0, [])
        return result