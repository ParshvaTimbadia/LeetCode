'''

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.


'''





class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        
        [[0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]]
        
        [[0,1,1,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,0]]
        
        """
        count=0
        row= len(A)
        column= len(A[0])
        
        for i in range(row):
            if(A[i][0]==1):
                self.BoardDSF(A, i, 0)
            if(A[i][column-1]==1):    
                self.BoardDSF(A, i, column-1)
        
        
        for j in range(column):
            if(A[0][j]==1):
                self.BoardDSF(A, 0, j)
            if(A[row-1][j]==1):    
                self.BoardDSF(A, row-1, j)
        
        
        for i in range(row):
            for j in range(column):
                if(A[i][j]==1):
                    count+=1
                    
        
        return count
    
    def BoardDSF(self,A, i, j ):
        
        if(i<0 or j<0 or i>len(A)-1 or j>len(A[0])-1):
            return; 
        
        if (A[i][j]==1):
            A[i][j]=-1
        
        if(i>0 and A[i-1][j]==1):
            self.BoardDSF(A, i-1, j)
        
        if(i<len(A)-1 and A[i+1][j]==1):
            self.BoardDSF(A, i+1, j)
        
        if(j>0 and A[i][j-1]==1):
            self.BoardDSF(A, i, j-1)
        
        if(j<len(A[0])-1 and A[i][j+1]==1):
            self.BoardDSF(A, i, j+1)
        
        return;
        
      
