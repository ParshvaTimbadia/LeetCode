class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # O(n x m)
        
        #hello
        #
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle:
                return i 
        
        return -1
                
            