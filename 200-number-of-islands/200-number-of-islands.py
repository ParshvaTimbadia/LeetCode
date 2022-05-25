class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        def dfs(row, col):
            
            if not(0 <= row < len(grid) and 0<=col<len(grid[0])) or (row, col) in visited or grid[row][col] != "1":
                return
        
            #Mark current node visited:
            visited.add((row, col))
            #Call negihbours
            dfs(row+1, col)
            dfs(row,col+1)
            dfs(row-1, col)
            dfs(row, col-1)
            
            
            
            
        visited = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == "1":
                    if (row, col) not in visited:
                        count += 1
                        dfs(row, col)
        
        return count
            
        