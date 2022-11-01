class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        row = [set() for i in range(len(matrix))]
        col = [set() for i in range(len(matrix[0]))]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                
                if 1 <= matrix[r][c] <= len(matrix):
                    row[r].add(matrix[r][c])
                    col[c].add(matrix[r][c])
        
        
        for i in row:
            if len(i) != len(matrix):
                return False
        
        for i in col:
            if len(i) != len(matrix[0]):
                return False
        
        return True