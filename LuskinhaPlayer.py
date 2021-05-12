from random import randint
from Player import Player

class BigBrainMoves(Player):

    def name(self):
        return "LuskinhaPlayer"

    def nextMove(self, board, player_code):
        bestScore = -10
        bestMove = 0
        isMax = True
        for i in range(9):
            if player_code == 2:
                isMax = False
            if board[i] == 0:
                board[i] = player_code
                score = self.minimax(board, 0, isMax, player_code)
                board[i] = 0
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        return bestMove
    
    def move(self, player_code, board):
        play = self.nextMove(board, player_code)
        return play


    def hasWinner(self, board):
        if((board[0] == board[1] == board[2]) & (board[0] != 0)):
            return True
        elif((board[3] == board[4] == board[5]) & (board[3] != 0)):
            return True
        elif((board[6] == board[7] == board[8]) & (board[6] != 0)):
            return True
        elif((board[0] == board[3] == board[6]) & (board[0] != 0)):
            return True
        elif((board[1] == board[4] == board[7]) & (board[1] != 0)):
            return True
        elif((board[2] == board[5] == board[8]) & (board[2] != 0)):
            return True
        elif((board[0] == board[4] == board[8]) & (board[0] != 0)):
            return True
        elif((board[2] == board[4] == board[6]) & (board[2] != 0)):
            return True
        else:
            return False
        
    def check_player_win(self, code, board):
        if((board[0] == board[1] == board[2]) & (board[0] == code)):
            return True
        elif((board[3] == board[4] == board[5]) & (board[3] == code)):
            return True
        elif((board[6] == board[7] == board[8]) & (board[6] == code)):
            return True
        elif((board[0] == board[3] == board[6]) & (board[0] == code)):
            return True
        elif((board[1] == board[4] == board[7]) & (board[1] == code)):
            return True
        elif((board[2] == board[5] == board[8]) & (board[2] == code)):
            return True
        elif((board[0] == board[4] == board[8]) & (board[0] == code)):
            return True
        elif((board[2] == board[4] == board[6]) & (board[2] == code)):
            return True
        else:
            return False

    def isDraw(self, board):
        for i in range(0,9):
            if board[i] == 0:
                return False
        if self.hasWinner(board):
            return False
        else:
            return True

    def invert_code(self, player_code):
        if player_code == 1:
            code = 2
        elif player_code == 2:
            code = 1
        return code

    def minimax(self, board, depth, isMax, player_code):

        if self.check_player_win(player_code, board):
            return 100
        elif self.check_player_win(self.invert_code(player_code), board):
            return -100
        elif self.isDraw(board):
            return 0
        
        if isMax:
            bestScore = -800
            for i in range(9):
                if board[i] == 0:
                    board[i] = player_code
                    score = self.minimax(board, depth + 1, False, player_code)
                    #print(board)
                    board[i] = 0
                    if score > bestScore:
                        bestScore = score
            return bestScore
        
        else:
            bestScore = 800
            for i in range(9):
                if board[i] == 0:
                    board[i] = player_code
                    score = self.minimax(board, depth + 1, True, self.invert_code(player_code))
                    board[i] = 0
                    if score < bestScore:
                        bestScore = score
            return bestScore
            



    


