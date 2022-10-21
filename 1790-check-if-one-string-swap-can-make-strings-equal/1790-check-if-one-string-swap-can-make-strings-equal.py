class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
    
        if len(s1) != len(s2):
            return False
        
        indexes = []
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                indexes.append(i)
        
        if len(indexes) == 0:
            return True
        
        if len(indexes) < 2 or len(indexes) > 2:
            return False
        
        if s1[indexes[0]] != s2[indexes[1]] or s1[indexes[1]] != s2[indexes[0]]:
            return False
        
        return True