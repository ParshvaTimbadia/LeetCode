class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        """
        Inference: 
        - Since X plays first at any point abs(count(X) - count(O)) <= 1
        - Game Ends: 
            - When n same characters are found horizontally or vertically or diagonally.
            if gameEnds with X: 
                - count(X) == count(O) + 1
            if gameEnds with O:
                - count(X) == count(O)
        
        """
        
        countX = 0
        countO = 0
        Xwins = False
        Owins = False
        
        for row in range(len(board)):
            for col in range(len(board)):
                
                if board[row][col] == "O":
                    countO += 1
                elif board[row][col] == "X":
                    countX += 1
            
            #Check for horizontal
            if board[row] == "XXX":
                Xwins = True
            elif board[row] == "OOO":
                Owins = True
                
            #Check for vertical
            vertical = "".join([board[0][row] + board[1][row] + board[2][row]])
            if vertical == "XXX":
                Xwins = True
            elif vertical == "OOO":
                Owins = True
        
        diagonal = "".join([board[0][0] + board[1][1] + board[2][2]])
        antidiagonal = "".join([board[0][2] + board[1][1] + board[2][0]])
        
        if diagonal == "XXX" or antidiagonal == "XXX":
            Xwins = True
        elif diagonal == "OOO" or antidiagonal == "OOO":
            Owins = True
        
        if Xwins:
            # if x_wins, for it to be a valid state, o should not win and since x plays first o should be one turn behind x
            return not Owins and countO == countX - 1
        elif Owins:
            # if o wins, then it should have played same turns as x
            return countX == countO
        
        # if no one won, the board to be a valid state, both turns could be same or x_turn could be greater by atmost 1  
        return countX >= countO and countX - countO <= 1

            
            
        
        
        
                    