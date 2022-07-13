class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0]) - 1] == 1:
            return -1
    
        visited = set()
        queue = deque()
        queue.append((0,0,1))
        visited.add((0,0))
        
        
        neighbours = [(1, 0), (0,1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while queue:
            
            row, col, distance = queue.popleft()
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return distance
            
            for r, c in neighbours:
                
                if not( 0<= row + r < len(grid) and 0 <= col + c < len(grid[0])) or (row+r,col+c) in visited or grid[row+r][col+c] == 1:
                    continue
                
                queue.append((row+r, col+c, distance + 1))
                visited.add((row+r, col+c))
        
        return -1
                
                
            
            
                
                
                
                