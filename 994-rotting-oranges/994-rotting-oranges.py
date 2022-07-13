class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        queue = deque()
        visited = set()
        count_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
                    count_oranges += 1
                elif grid[row][col] == 1:
                    count_oranges += 1
        
        days = -1
        while queue:
            
            for _ in range(len(queue)):
                
                row, col  = queue.popleft()
                
                if row - 1 >= 0 and (row-1, col) not in visited and grid[row-1][col] == 1:
                    visited.add((row-1, col))
                    queue.append((row-1, col))
                
                if row + 1 < len(grid) and (row+1, col) not in visited and grid[row+1][col] == 1:
                    visited.add((row+1, col))
                    queue.append((row+1, col))
                    
                if col - 1 >= 0 and (row, col-1) not in visited and grid[row][col-1] == 1:
                    visited.add((row, col-1))
                    queue.append((row, col-1))
                    
                if col + 1 < len(grid[0]) and (row, col+1) not in visited and grid[row][col+1] == 1:
                    visited.add((row, col+1))
                    queue.append((row, col+1))
                
            days += 1
        
       
        return max(days,0) if len(visited) == count_oranges else -1