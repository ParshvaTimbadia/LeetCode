class Solution:
    def partition(self, s: str) -> List[List[str]]:
            
        
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end] : 
                    return False
                start += 1
                end -= 1
            return True
            
            
        
        #RecursiveApproach
        result = []
        
        def helper(index, slate):
            
            if index == len(s):
                result.append(slate[:])
                return
            
            for i in range(index, len(s)):
                
                prefix = s[index:i+1]
                
                if isPalindrome(index, i):
                    slate.append(prefix)
                    helper(i+1,slate)
                    slate.pop()
        
        helper(0,[])
        return result
        
                    
            
            