class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs, key = lambda x: x[0]-x[1]) # More negative means more b cost mare and a cost less
        
        result = 0
        for i in range(len(costs)//2):
            result += costs[i][0]
        
        for i in range(len(costs)//2, len(costs)):
            result += costs[i][1]
        
        return result
            