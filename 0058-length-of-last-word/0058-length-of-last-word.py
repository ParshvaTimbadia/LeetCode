class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lastWordLength = 0
        
        s += " "
        count = 0
        for i in range(len(s)):
            if s[i].isalpha():
                count += 1
            else:
                if count > 0:
                    lastWordLength = count
                    count = 0
        
        return lastWordLength
                
                
                