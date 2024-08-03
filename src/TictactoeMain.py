import random

class TictactoeMain():
    #CONSTANTS ------------------
    COMP = 'O'
    HUMAN = "X"
    BOARD = [[" " for _ in range(3)] for _ in range(3)]

    #PRINT BOARD -----------------
    def printBoard(self, board):
        for row in board:
            print(" | ".join(row))
            print("---------")

    #POSITION -------------------
    def getPosition(self, position):
        row = (int)(position - 1) // 3
        col = (int)(position - 1) % 3
        return row, col

    #DECLARE WINNER -----------------
    def declareWinner(self, board):
        for y in range(3):
            # Check horizontal lines
            if (board[y][0] == board[y][1] == board[y][2]) and (board[y][0]!= " "):
                return board[y][0]
            # check vertical lines
            if (board[0][y] == board[1][y] == board[2][y]) and (board[0][y]!= " "):
                return board[0][y]
        # Check diagonals
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0]!= " "):
            return board[0][0]
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2]!= " "):
            return board[0][2]
        return None 

    #TERMINAL STATE -------------
    def terminalState(self, board):
        # Check if X or O wins
        winner = self.declareWinner(board)
        if winner is not None:
            return True
        else:
            # Check if the board is full (tie)
            for row in board:
                for cell in row:
                    if cell == " ":
                        return False
            return True

    #PLAYER MOVE -------------------
    def playerMove(self, board, position):
        self.insertLetter(board, self.HUMAN, position)
        return

    #INSET LETTER ------------------
    def insertLetter(self, board, player, position):
        row, col = self.getPosition(position)
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print(player, position, "This position is invalid, please try again")

    #IS SPACE FREE -----------------
    def isSpaceEmpty(self, board, position):
        row, col = self.getPosition(position)
        if board[row][col] == " ":
            return True
        else:
            return False

    #COMP MOVE ----------------------
    #find best score
    def computerMove(self, board):
        bestScore = -1000
        bestMove = 0
        for i in range(1, 10):
            if self.isSpaceEmpty(board, i):
                row, col = self.getPosition(i)
                board[row][col] = self.COMP
                score = self.minimax(board, False, 0, -1000, 1000)
                board[row][col] = " "
                if (score > bestScore):
                    bestScore = score
                    bestMove = i
        self.insertLetter(board, self.COMP, bestMove)
        return

    #UTILITY FUNCTION
    def utility(self, board, depth):
        result = self.declareWinner(board)
        if result == 'X':
            return -10 + depth
        if result == 'O':
            return 10 - depth
        if (self.terminalState(board)) and (result!= 'X') and (result!= 'O'):
            return 0

    #MINIMAX FUNCTION --------------
    def minimax(self, board, isMaximising, depth, alpha = -1000, beta = 1000):
        if self.terminalState(board):
            return self.utility(board, depth)
        
        if(isMaximising): #maximising score
            bestScore = -1000
            for i in range(1, 10): # iterate over positions 1 to 9
                if self.isSpaceEmpty(board, i):
                    row, col = self.getPosition(i)
                    board[row][col] = self.COMP
                    score = self.minimax(board, False,depth+1, alpha, beta)
                    board[row][col] = ' '
                    bestScore = max(bestScore, score)
                    alpha = max(alpha, bestScore)
                    if beta <= alpha:
                        break
            return bestScore
        else: #minimising
            bestScore = 1000
            for i in range(1, 10): # iterate over positions 1 to 9
                if self.isSpaceEmpty(board, i):
                    row, col = self.getPosition(i)
                    board[row][col] = self.HUMAN
                    score = self.minimax(board, True,depth+1,  alpha, beta)
                    board[row][col] = ' '
                    bestScore = min(bestScore, score)
                    beta = min(beta, bestScore)
                    if beta <= alpha:
                        break
            return bestScore


    # def main():
    #     #random_number = random.randint(1, 9)
    #     #insertLetter(BOARD, COMP, random_number)

    #     while not TictactoeMain.terminalState(TictactoeMain.BOARD):
    #         TictactoeMain.printBoard(TictactoeMain.BOARD)
    #         TictactoeMain.playerMove(TictactoeMain.BOARD)
    #         if not TictactoeMain.terminalState(TictactoeMain.BOARD):
    #             TictactoeMain.computerMove(TictactoeMain.BOARD)
    #         else:
    #             break

    #     TictactoeMain.printBoard(TictactoeMain.BOARD)
    #     print("Winner is:", TictactoeMain.declareWinner(TictactoeMain.BOARD))

