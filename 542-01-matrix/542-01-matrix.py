from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        visited = set()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row,col,0))
        
        while queue:
            
            row, col, distance = queue.popleft()
            
            if not (0<= row < len(mat) and 0 <= col < len(mat[0])):
                continue
            
            if (row, col) in visited:
                continue
                
            mat[row][col] = distance
            
            visited.add((row, col))
            
            queue.append((row+1, col, distance+1))
            queue.append((row-1, col, distance+1))
            queue.append((row, col+1, distance+1))
            queue.append((row, col-1, distance+1))
        
        return mat
            
            
            
                    