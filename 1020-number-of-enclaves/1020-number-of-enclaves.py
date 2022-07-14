class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != 1:
                return
            
            grid[row][col] = -1
            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1) 
        
        
        count_ones = 0
        
        for row in range(len(grid)):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][len(grid[0])-1] == 1:
                dfs(row, len(grid[0])-1)

        for col in range(len(grid[0])):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[len(grid)-1][col] == 1:
                dfs(len(grid)-1, col)
        
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if grid[row][col] == 1:
                    count_ones += 1
        
        return count_ones
                    