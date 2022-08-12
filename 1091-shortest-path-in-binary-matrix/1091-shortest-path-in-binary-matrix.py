class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        queue = deque()
        queue.append((0,0))
        visited = set((0,0))
        
        
        neighbors = [(0,1), (1,0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        distance = 1
        
        while queue:
            
            for _ in range(len(queue)):
                
                row, col = queue.popleft()
                
                
                if row == n - 1 and col == n - 1:
                    return distance
                
                for r, c in neighbors:
                    
                    if not(0 <= row + r < n and 0 <= col + c < n) or (row + r, col + c) in visited or grid[row + r][col + c]==1:
                        continue
                    
                    visited.add((row + r, col + c))
                    queue.append((row + r, col + c))
                    
        
            distance += 1
        
        
        return -1
            
            
            
            