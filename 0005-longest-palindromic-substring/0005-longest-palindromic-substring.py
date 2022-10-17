class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        
        start = -1
        maxLength = 1

        #Interestingly, every individual letter will be a palindrome.

        for i in range(len(s)):
            dp[i][i] = True

        for startIndex in range(len(s) - 1, -1, -1):
            for endIndex in range(startIndex + 1, len(s)):

                if s[startIndex] == s[endIndex]:
                    if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                        dp[startIndex][endIndex] = True
                        
                        if endIndex - startIndex + 1 > maxLength:
                            maxLength = max(maxLength, endIndex - startIndex + 1)
                            start = startIndex
                        

        return s[start: start+maxLength] if maxLength > 1 else s[0]