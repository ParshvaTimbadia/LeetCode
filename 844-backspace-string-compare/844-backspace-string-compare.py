class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextLetter(word, pointer):
            countBackSpaces = 0
            while pointer >= 0:
                if word[pointer] == "#":
                    countBackSpaces += 1
                elif countBackSpaces > 0:
                    countBackSpaces -= 1
                else:
                    break
                pointer -= 1

            return pointer
    
        pointer1 = len(s)-1
        pointer2 = len(t)-1

        while pointer1 > -1 or pointer2 > -1:
            
            getNextValidLetter_s = nextLetter(s, pointer1)
            getNextValidLetter_t = nextLetter(t, pointer2)
            
            if getNextValidLetter_s < 0 and getNextValidLetter_t < 0:
                return True
            
            if s[getNextValidLetter_s] != t[getNextValidLetter_t]:
                return False
            
            if getNextValidLetter_s < 0 or getNextValidLetter_t < 0:
                return False
            
            pointer1 = getNextValidLetter_s - 1
            pointer2 = getNextValidLetter_t - 1

                
        if pointer1 == pointer2 :
            return True

        