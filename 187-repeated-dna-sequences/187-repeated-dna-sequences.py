from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []
        
        current_window = []
        hMap = defaultdict(int)
        for i in range(10):
            current_window.append(s[i])
        
        i+=1
        hMap["".join(current_window)] += 1
        
        while i < len(s):
            
            current_window.pop(0)
            current_window.append(s[i])
            
            if len(current_window) == 10:
                hMap["".join(current_window)] += 1
        
            i+=1
        
        
        result = [key for key, value in hMap.items() if value > 1]
        return result
            
            
        """
        TimeComplexity: O(N)
        SpaceComplexity: O(L(N-L))
        
        """
        