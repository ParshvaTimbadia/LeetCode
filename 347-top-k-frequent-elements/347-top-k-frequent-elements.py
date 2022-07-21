class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = collections.Counter(nums)
        
        minHeap = []
        for key, value in dict.items():
            if len(minHeap) < k:
                heappush(minHeap, (value, key))
            elif minHeap[0][0] < value:
                heappop(minHeap)
                heappush(minHeap, (value, key))
        
        result = []
        while minHeap:
            result.append(heappop(minHeap)[1])
        
        return result