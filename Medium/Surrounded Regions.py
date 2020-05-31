'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


'''

class Solution(object):
    def solve(self, board):
        
        if len(board)==0:
            return []
        
        row = len(board)
        column= len(board[0])
        
        for i in range(row):
            if(board[i][0]=='O'):
                self.BoardDSF(board, i, 0)
            if(board[i][column-1]=='O'):    
                self.BoardDSF(board, i, column-1)
        
        
        for j in range(column):
            if(board[0][j]=='O'):
                self.BoardDSF(board, 0, j)
            if(board[row-1][j]=='O'):    
                self.BoardDSF(board, row-1, j)
                
        for i in range(row):
            for j in range(column):
                if(board[i][j]=='O'):
                    board[i][j]='X'
                elif(board[i][j]=='*'):
                    board[i][j]='O'    
                    
    def BoardDSF(self,board, i, j ):
        
        if(i<0 or j<0 or i>len(board)-1 or j>len(board[0])-1):
            return; 
        
        if (board[i][j]=='O'):
            board[i][j]='*'
        
        if(i>0 and board[i-1][j]=='O'):
            self.BoardDSF(board, i-1, j)
        
        if(i<len(board)-1 and board[i+1][j]=='O'):
            self.BoardDSF(board, i+1, j)
        
        if(j>0 and board[i][j-1]=='O'):
            self.BoardDSF(board, i, j-1)
        
        if(j<len(board[0])-1 and board[i][j+1]=='O'):
            self.BoardDSF(board, i, j+1)
        
        return;
        
