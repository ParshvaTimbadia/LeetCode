class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        [10, -5] => [10]
        [5, -5] => []
        [5, -10] => [-10]
        
        """
        
        stack = []
        value = None
        for new in asteroids:
            value = new
            while stack and new < 0 < stack[-1]:
                if abs(new) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(new) == abs(stack[-1]):
                    stack.pop()
                    value = None
                    break
                else:
                    value = None
                    break
            
            if value:
                stack.append(value)
        
        return stack
            
            
            
                    