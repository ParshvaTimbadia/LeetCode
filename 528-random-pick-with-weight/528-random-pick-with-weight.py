class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefixSum = 0
        
        for weight in w:
            prefixSum += weight
            self.prefix.append(prefixSum)
        self.total = prefixSum
        

    def pickIndex(self) -> int:
        
        random_num = self.total*random.random()
        low, high = 0, len(self.prefix) - 1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if self.prefix[mid] < random_num:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()