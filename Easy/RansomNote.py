***
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
***


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dict={}
        for i in range(len(magazine)):
            
            if magazine[i] not in dict:
                dict[magazine[i]]=0
            dict[magazine[i]]+=1
            
        for i in range(len(ransomNote)):
            
            if ransomNote[i] not in dict:
                return False
            else:
                dict[ransomNote[i]]-=1
                
            if dict[ransomNote[i]]<0:
                    return False
            
        return True       
