class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        array = [0]*2051
        
        for log in logs:
            start = log[0]
            end = log[1]
            array[start] += 1
            array[end] -= 1
        
        
        maxPopulation = 0
        prefixSum = 0
        bestPopulation = 0
        for index, num in enumerate(array):
            prefixSum += num
            if prefixSum > maxPopulation:
                bestPopulation = index
                maxPopulation = max(prefixSum, maxPopulation)
        
        return bestPopulation
            