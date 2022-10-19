class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        direction = 0
        
        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up
        
        while top <= bottom and left <= right: #Condition TBA
            
            if direction == 0:
                for i in range(left,right+1):
                    result.append(matrix[top][i])
                top += 1
                  
            if direction == 1:
                for i in range(top,bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            
            if direction == 2:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if direction == 3:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1
            
            direction = (direction + 1)%4
        
        return result
            
            
            
            