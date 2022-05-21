class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        store = collections.Counter(s1)
        match = 0
        start = 0
        
        for end, element in enumerate(s2):
            
            if element in store:
                store[element] -= 1
            
                if store[element] == 0:
                    match += 1
            
            if match == len(store):
                return True
            
            if end >= len(s1) - 1 :
                
                if s2[start] in store:
                    if store[s2[start]] == 0:
                        match -= 1
                    store[s2[start]] += 1
                    
                
                start += 1
        
        return False
                    