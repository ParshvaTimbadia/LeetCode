class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def checker(row, col, index):
            
            if index == len(word):
                return True
            
            if (row, col) in visited or not (0 <= row < len(board) and 0 <= col < len(board[0])):
                return False
            
            if word[index] != board[row][col]:
                return False
            
            visited.add((row,col))
            
            result = checker(row-1, col, index+1) or checker(row+1, col, index+1) or checker(row, col+1, index+1) or checker(row, col-1, index+1)
            
            visited.remove((row, col))
            
            return result
              
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if board[row][col] == word[0]:
                    if checker(row, col, 0):
                        return True
        
        return False
        
        