class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = 1
        col = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                
                if matrix[r][c] == 0:
                    if r == 0 or c == 0:
                        if r == 0:
                            row = 0
                        if c == 0:
                            col = 0
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
    
        if col == 0:   
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if row == 0: 
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        return matrix
                    
                        
            