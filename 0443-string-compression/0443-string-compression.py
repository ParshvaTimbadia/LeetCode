class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count = 1
        pointer = -1
        chars.append("_")
        for i in range(len(chars) -1):
            
            if chars[i] == chars[i+1]:
                count += 1
            elif count == 1:
                pointer += 1
                chars[pointer] = chars[i]
            else: #Counter > 1:
                pointer += 1
                chars[pointer] = chars[i]
                
                j = 0
        
                coutString = str(count)
                
                while j < len(coutString):
                    pointer += 1
                    chars[pointer] = coutString[j]
                    j+=1
                
                count = 1
        
        
        return pointer+1