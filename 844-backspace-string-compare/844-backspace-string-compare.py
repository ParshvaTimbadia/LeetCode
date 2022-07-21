class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            index1 = self.nextValidCharacter(s, i)
            index2 = self.nextValidCharacter(t, j)
            
            if index1 < 0 and index2 < 0:
                return True
            
            if index1 < 0 or index2 < 0:
                return False
            
            if s[index1] != t[index2]:
                return False
            
            i = index1 - 1
            j = index2 - 1

        
        return index1 == index2
    
    
    def nextValidCharacter(self, s, i):
        countBackSpaces = 0
        while i >= 0:
            if s[i] == "#":
                countBackSpaces += 1
                i -= 1
            elif countBackSpaces > 0:
                countBackSpaces -= 1
                i -= 1
            else:
                return i
        
        return i
        
            