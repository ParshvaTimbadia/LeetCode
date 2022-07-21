class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        #Find the width of the each element
        
        for row in range(len(mat)):
            for col in range(len(mat[0])-2, -1, -1):
                if mat[row][col] == 1:
                    mat[row][col] = mat[row][col+1] + 1
                    
        
        count = 0        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                minDepth = mat[row][col]
                
                for depth in range(row, len(mat)):
                    
                    if mat[depth][col] == 0:
                        break
                    
                    minDepth = min(minDepth, mat[depth][col])
                    count += minDepth
                
        return count
                
                
        