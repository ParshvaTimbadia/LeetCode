class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for point in points:
            if len(maxHeap) < k:
                heappush(maxHeap, (-self.getDistance(point[0], point[1]), point))
            elif -maxHeap[0][0] > self.getDistance(point[0], point[1]):
                heappop(maxHeap)
                heappush(maxHeap,(-self.getDistance(point[0], point[1]), point))
        result = []
        while maxHeap:
            result.append(heappop(maxHeap)[1])
        
        return result
        
                
    
    
    def getDistance(self, x, y):
        return x*x + y*y