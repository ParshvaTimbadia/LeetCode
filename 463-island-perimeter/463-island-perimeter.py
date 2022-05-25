class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        def dfs(row, col):
            
            if not(0 <= row < len(grid) and 0<= col < len(grid[0])) or grid[row][col] == 0:
                return 1 
            
            if (row, col) in visited:
                return 0
            
            visited.add((row,col))
            
            return dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        bestPerimeter = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1 and (row,col) not in grid:
                    bestPerimeter = max(bestPerimeter, dfs(row, col))
        
        return bestPerimeter