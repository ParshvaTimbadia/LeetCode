class Solution:
    def lastRemaining(self, n: int) -> int:
        
        head = 1
        remain = n
        left = True
        step = 1
        while remain > 1:
            
            if left or remain%2 == 1:
                head += step
            
            remain //= 2
            left = not left
            step *= 2
        
        return head
                