class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        
        def dfs(row, col):
            
            if not(0 <= row < len(grid) and 0 <= col < len(grid[0])) or (row, col) in visited or grid[row][col] == 1:
                return
            
            visited.add((row, col))
            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        
        visited = set()
        count = 0
        
        for row in range(len(grid)):
            if grid[row][0] == 0:
                dfs(row, 0)
            
            if grid[row][len(grid[0])-1] == 0:
                dfs(row, len(grid[0])-1)
        
        for col in range(len(grid)):
            
            if grid[0][col] == 0:
                dfs(0, col)
            
            if grid[len(grid)-1][col] == 0:
                dfs(len(grid)-1, col)
                
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0])-1):
                
                if grid[row][col] == 0:
                    if (row, col) not in visited:
                        count += 1
                        dfs(row, col)
        
        return count
        
        
                