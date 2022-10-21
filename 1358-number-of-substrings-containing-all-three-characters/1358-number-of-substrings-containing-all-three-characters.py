class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        index_a = -1
        index_b = -1
        index_c = -1
        count = 0
        
        for index, char in enumerate(s):
            
            if char == "a":
                index_a = index
            elif char == "b":
                index_b = index
            elif char == "c":
                index_c = index
            
            count += min(index_a, index_b, index_c) + 1
        
        return count
        