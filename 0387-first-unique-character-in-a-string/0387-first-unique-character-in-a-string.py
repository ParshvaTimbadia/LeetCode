class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        seen = collections.Counter(s)
        
        for index, char in enumerate(s):
            if seen[char] == 1:
                return index
        
        return -1