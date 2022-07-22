class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        while i <= j:
            
            while i < len(s) and not s[i].isalnum():
                i += 1
            
            while j >= 0 and not s[j].isalnum():
                j -= 1
                
            if 0 <= i < len(s) and 0 <= j <len(s) and s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
        
        return True
                    