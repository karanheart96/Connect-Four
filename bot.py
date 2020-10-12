import math
from board import Board
import random


# This is the parent class for your AI bots.
class Bot:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # return a list of children and moves that generate them
    def generateChildren(self, board):
        children = []
        i = 0
        while(i<board.width):
            if len(board.board[i]) <= board.height:
                new_board = Board(board)
                new_board.makeMove(i)
                children.append([i, new_board])
            i+=1

        return children

# In this class implement the minimax algorithm with cutoff
class minMaxCutoffBot(Bot):
    
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return the optimal column to move in
    def findMove(self, board):
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        return move

    # findMove helper function - minimax
    def miniMax(self, board, depth, player):
        if board.isFull():
            return (board.heuristic(),-1)
        if depth <= 0:
            return (board.heuristic(),-1)
        g = board.isGoal()
        if g>=0:
            return (g,-1)
        if player==1:
            bestval = -math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.miniMax(child,depth-1, 2)
                if bestval < bestScore:
                    bestval = bestScore
                    bestColumn = column
            return (bestval, bestColumn)
        else:
            bestval = math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.miniMax(child,depth-1, 1)
                if bestval > bestScore:
                    bestval = bestScore
                    bestColumn = column
            return (bestval, bestColumn)



# In this class implement the alpha beta pruning algorithm with cutoff
class alphaBetaCutoffBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in
    def findMove(self, board):
        score, move = self.alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf)
        return move

    # findMove helper function - alpha beta pruning
    def alphaBeta(self, board, depth, player, alpha, beta):
        if board.isFull():
            return (board.heuristic(),-1)
        if depth <= 0:
            return (board.heuristic(),-1)
        g = board.isGoal()
        if g>=0:
            return (g,-1)
        if player==1:
            bestval = -math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.alphaBeta(child,depth-1, 2, alpha, beta)
                if bestval < bestScore:
                    bestval = bestScore
                    bestColumn = column
                if bestval > alpha:
                    alpha = bestval
                    bestColumn = column
                if alpha >= beta:
                    break
            return (bestval, bestColumn)
        else:
            bestval = math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.alphaBeta(child,depth-1, 1, alpha, beta)
                if bestval > bestScore:
                    bestval = bestScore
                    bestColumn = column
                if bestval < beta:
                    beta = bestval
                    bestColumn = column
                if alpha >= beta:
                    break
            return (bestval, bestColumn)

# In this class implement the alpha beta pruning algorithm
class alphaBetaBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in
    def findMove(self, board):
        score, move = self.alphaBetaVanila(board, self.isPlayerOne, -math.inf, math.inf)
        return move

    # findMove helper function - alpha beta pruning
    def alphaBetaVanila(self, board, player, alpha, beta):
        if board.isFull():
            return (board.heuristic(),-1)
        g = board.isGoal()
        if g>=0:
            return (g,-1)
        if player==1:
            bestval = -math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.alphaBetaVanila(child, 2, alpha, beta)
                if bestval < bestScore:
                    bestval = bestScore
                    bestColumn = column
                if bestval > alpha:
                    alpha = bestval
                    bestColumn = column
                if alpha >= beta:
                    break
            return (bestval, bestColumn)
        else:
            bestval = math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.alphaBetaVanila(child, 1, alpha, beta)
                if bestval > bestScore:
                    bestval = bestScore
                    bestColumn = column
                if bestval < beta:
                    beta = bestval
                    bestColumn = column
                if alpha >= beta:
                    break
            return (bestval, bestColumn)

# In this class implement the minimax algorithm
class minMaxBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return the optimal column to move in
    def findMove(self, board):
        score, move = self.miniMaxVanila(board, self.isPlayerOne)
        return move

    # findMove helper function - minimax
    def miniMaxVanila(self, board, player):
        if board.isFull():
            return (board.heuristic(),-1)
        g = board.isGoal()
        if g>=0:
            return (g,-1)
        if player==1:
            bestval = -math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.miniMaxVanila(child, 2)
                if bestval < bestScore:
                    bestval = bestScore
                    bestColumn = column
            return (bestval, bestColumn)
        else:
            bestval = math.inf
            bestColumn = -1
            children = super().generateChildren(board)
            for column, child in children:
                bestScore, column_n = self.miniMaxVanila(child, 1)
                if bestval > bestScore:
                    bestval = bestScore
                    bestColumn = column
            return (bestval, bestColumn)



# random bot
class randomBot(Bot):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # return a random column to move in
    def findMove(self, board):
        move = random.randint(0, board.width - 1)
        while len(board.board[move]) == board.height:
            move = random.randint(0, board.width - 1)
        return move

# human player
class HumanPlayer:

    def __init__(self, depthLimit, isPlayerOne):
        pass

    def findMove(self, board):
        pass
