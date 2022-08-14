class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        hMap = {}
        maxLength = 0
        for end in range(len(s)):
            
            if s[end] not in hMap:
                hMap[s[end]] = end
            else:
                start = max(start, hMap[s[end]] + 1)
            
            hMap[s[end]] = end
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
            
            
            
            
            
                
            