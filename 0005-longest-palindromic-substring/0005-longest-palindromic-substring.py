class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        #TC- O(N2)
        #SC - O(1)
        
        
        # aba
        #  ^
        # abba
        #  ^^
        
        def expandAroundCenter(start, end):
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            start += 1
            end -= 1
            return end - start + 1, start, end
        
        maxLength = 0
        result = ""
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i+1)
            length, start, end = max(len1, len2)
            if maxLength < length:
                result = s[start:end+1]
                maxLength = max(maxLength, length)
        
        return result
        
            
            
            