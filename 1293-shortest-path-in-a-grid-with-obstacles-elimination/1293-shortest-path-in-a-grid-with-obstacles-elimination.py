from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # BFS for sure.
        
        seen = set()
        queue = deque()
        queue.append((0, 0, 0, k))
        mindist = math.inf
        
        
        while queue:
            
            row, col, distance, k = queue.popleft()
            
            
            if not(0 <= row < len(grid) and 0 <= col < len(grid[0])) or k < 0 or (row, col, k) in seen:
                continue
                
            seen.add((row, col, k))
            
            if grid[row][col] == 1:
                k -= 1
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1 and k >= 0:
                return distance
            
            queue.append((row+1, col, distance+1, k))
            queue.append((row-1, col, distance+1, k))
            queue.append((row, col+1, distance+1, k))
            queue.append((row, col-1, distance+1, k))
            
            
        
        return -1
            
            
                