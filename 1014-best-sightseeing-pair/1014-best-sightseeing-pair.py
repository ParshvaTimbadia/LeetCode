class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        # (values[i] + i)+ (values[j] -j)
        
        best = values[0]
        score = 0
        for j in range(1, len(values)):
            score = max(score, best + values[j] - j)
            best = max(best, values[j] + j)
        
        return score