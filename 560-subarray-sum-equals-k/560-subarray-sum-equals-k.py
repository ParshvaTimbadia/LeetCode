class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        #[5, 5, -5] , k = 5
        #  ^
        
        hMap = {0:1}
        totalSum = 0
        result = 0
        
        for num in nums:
            totalSum += num
            if  totalSum - k in hMap:
                result += hMap[totalSum - k]
            
            if totalSum not in hMap:
                hMap[totalSum] = 0
            hMap[totalSum] += 1
        
        return result
                