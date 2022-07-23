class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = []
        
        dir = 0
        while left <= right and top <= bottom:
            
            if dir == 0:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
            elif dir == 1:
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            elif dir == 2:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            
            dir = (dir + 1)%4
        
        return result