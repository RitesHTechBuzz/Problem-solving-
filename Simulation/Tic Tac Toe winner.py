# To determine the winner of tic tac toe game between two players A and B or else return draw if all moves utilised 
from typing import List

def tictactoe(self,moves:List[List[int]])->str:
    board =[[" "for _ in range(3)]for _ in range(3)]

    def check_winner(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
            if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
                return True
        return False
    
    for i,(row,col) in enumerate(moves):
        player = 'X'if i%2==0 else 'O'
        board[row][col] = player
        if check_winner(player):
            return 'A' if player =='X'else 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'