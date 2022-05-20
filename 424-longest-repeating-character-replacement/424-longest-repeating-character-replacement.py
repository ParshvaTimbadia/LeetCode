class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        start = 0
        maxRepeatingCharacter = 0
        maxLength = 0
        for end, element in enumerate(s):
            
            if element not in store:
                store[element] = 0
            store[element] += 1
            maxRepeatingCharacter = max(maxRepeatingCharacter, store[element])
            
            while end - start - maxRepeatingCharacter + 1 > k:
                store[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
        return maxLength
            
            