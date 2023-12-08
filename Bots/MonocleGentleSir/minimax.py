from connect4 import Connect4
import random

INF = 1000000

class Bot:
    def __init__(self):
        self.board = None
        self.bestMove = None
        self.startTime = None
    

    def choose_move(self, board):
        self.board = board

        legal_moves = list(self.board.legal_moves)
        self.bestMove = random.choice(legal_moves)

        for i in range(7):
            for j in range(6):
                print(self.board.grid[j][i])

        self.search(4, 0)

        return self.bestMove 


    def search(self, depth, ply):
        if self.board.is_win():
            return -INF
        if self.board.is_draw():
            return 0

        if depth <= 0:
            return self.evaluate()


        moves = list(self.board.legal_moves)
        random.shuffle(moves)
        bestScore = -INF-1
        for move in moves:
            self.board.push(move)
            score = -self.search(depth-1, ply+1)
            self.board.pop()

            if score > bestScore:
                bestScore = score
                if ply == 0: self.bestMove = move


        return score
    
    def evaluate(self):
        score = 0
        for i in range(7):
            for j in range(6):
                if self.board.grid[j][i] == 0:
                    score += 1
                elif self.board.grid[j][i] != 0:
                    score -= 1
        return score