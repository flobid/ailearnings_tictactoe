"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if sum([item is not None for sublist in board for item in sublist])%2:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i,j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] is None]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if (action in actions(board)):
        (i,j) = action
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("The action is not valid")
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i].count(board[i][0])==3 and board[i][0]!=None:
            return board[i][0]
        elif [row[i] for row in board].count(board[0][i])==3 and board[0][i]!=None:
            return board[0][i]
    first_diag = [board[0][0],board[1][1],board[2][2]]
    second_diag = [board[2][0],board[1][1],board[0][2]]
    if first_diag.count(board[0][0])==3 and board[0][0]!=None:
        return board[0][0]
    elif second_diag.count(board[2][0])==3 and board[2][0]!=None:
        return board[2][0]
    else:
        return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return sum([none_per_row.count(None) for none_per_row in board])==0 or winner(board)!=None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return (winner(board)=="X") - (winner(board)=="O")

def min_value(board,v):
    """
    Returns the minimizing choice
    """
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,max_value(result(board,action),v))
    return v


def max_value(board,v):
    """
    Returns the maximizing choice
    """
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,min_value(result(board,action),v))
    return v
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "O":
        for action in actions(board):
            if min_value(result(board,action),float('inf'))==-1:
                return action
        for action in actions(board):
            if min_value(result(board,action),float('inf'))==0:
                return action
            

    else:
        for action in actions(board):
            if max_value(result(board,action),float('-inf'))==1:
                return action
        for action in actions(board):
            if max_value(result(board,action),float('-inf'))==0:
                return action
        
