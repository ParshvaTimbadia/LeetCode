class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        
        # Algorithm:
        # Sliding Window based question
        # Fixed Size string. 
        
        startWindow = 0
        seen = set()
        result = set()
        for endWindow in range(len(s)):
            
            if endWindow >= 9:
                DNA = s[startWindow:endWindow+1]
                if DNA in seen:
                    result.add(DNA)
                seen.add(DNA)
                startWindow += 1
        
        return result