class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #this solution occupies O(N) space since we are changing the array
        
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed)-1):
            
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            
        
        return True if n <= 0 else False
    