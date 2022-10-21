class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        minHeap = []
        for index in range(len(heights)-1):
            diff = heights[index+1] - heights[index]
            if diff > 0:
                heappush(minHeap, diff)
            if len(minHeap) > ladders:
                bricks -= heappop(minHeap)
            if bricks < 0:
                return index
        
        return len(heights) - 1