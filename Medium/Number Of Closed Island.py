'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Link to the problems Statement: https://leetcode.com/problems/number-of-closed-islands/
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''



class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows= len(grid)
        colums= len(grid[0])
        count=0
        
        for i in range(1,rows):
            for j in range(1,colums):
                if(grid[i][j]==0):
                    if(self.checkisClosed(grid, i, j)):
                        count+=1
        return count
        
    def checkisClosed(self, grid, i, j):
        #Include Some base case here
        if(grid[i][j]==-1 or grid[i][j]==1):
            return True
        
        if(self.NotwithinBoundary(grid,i,j)):
            return False
        
        grid[i][j]=-1
        
        down = self.checkisClosed(grid, i+1, j)
        up = self.checkisClosed(grid, i-1, j)
        right= self.checkisClosed(grid, i, j+1)
        left = self.checkisClosed(grid, i, j-1)
        
        
        return down and up and right and left
    
    def NotwithinBoundary(self, grid, i, j):
        return i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1
