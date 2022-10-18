class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if n > 1:
                return False
            return True if flowerbed[0] == 0 else False
        
        
        flowerbed = flowerbed
        
        for i in range(len(flowerbed)):
            
            if (i == flowerbed[i] == flowerbed[i+1] == 0) or (i == len(flowerbed) -1 and flowerbed[i] == flowerbed[i-1] == 0) or (i > 0 and i < len(flowerbed) -1 and flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0):
                
                flowerbed[i] = 1
                n -= 1
        
        
        
        return True if n <= 0 else False
    