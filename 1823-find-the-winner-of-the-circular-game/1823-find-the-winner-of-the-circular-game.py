class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque()
        for i in range(1, n+1):
            queue.append(i)
        
        while len(queue)!=1:
            
            #Remove first K-1 elements from the queue.
            i = 0 
            while i != k -1:
                queue.append(queue.popleft())
                i += 1
            
            #Remove kth element
            queue.popleft()
        
        return queue[0]
    
        # TimeComplexity: O(N**2)
        # Space Complexity: Since we are using the queue of size N, it would be O(N).