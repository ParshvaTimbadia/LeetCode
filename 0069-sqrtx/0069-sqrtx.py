class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        start = 0
        end = x //2
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            sqrt = mid*mid
            
            if sqrt == x:
                return mid
            elif sqrt < x:
                start = mid + 1
            else:
                end = mid - 1
        
        return end
            