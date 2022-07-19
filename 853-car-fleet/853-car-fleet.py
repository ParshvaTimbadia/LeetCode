class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        
        -> ->           target miles
        [position, speed]
        
        
        """
        
        pair = [[p, (target - p)/s] for p,s in zip(position, speed)]
        pair.sort(key = lambda x : x[0])
        stack = []
        stack.append(pair[-1])
        for i in range(len(position)-2,-1,-1):
            if stack[-1][1] < pair[i][1]:
                stack.append(pair[i])
        
        return len(stack)
                