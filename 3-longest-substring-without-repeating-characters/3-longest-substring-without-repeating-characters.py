class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        hMap = {}
        length = 0
        for end in range(len(s)):
            char = s[end]
            if char not in hMap:
                hMap[char] = end
            else:
                start = max(hMap[char] + 1, start)
                hMap[char] = end
        
            length = max(length, end - start + 1)
        
        return length
        
    
                
            
            
            
            
                
                
            
            