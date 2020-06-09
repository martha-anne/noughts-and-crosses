import sys

# complete this enum with all the possible states of a noughts and crosses board (there's more than 3)
class BoardState:
NOUGHTS_WIN = 'NOUGHTS_WIN'
CROSSES_WIN = 'CROSSES_WIN'
DRAW = 'DRAW'
GAME_IN_PROGRESS = 'GAME_IN_PROGRESS' #This will be used in the case that there is no winner, but empty board spaces remain.
INVALID = 'INVALID' #This will be used in the case that the numer of Xs is not equal to or one greater than the number of Os.

# complete this function so that it returns the correct board state
def getStateOfBoard(board):
return BoardState.DRAW

# leave this part unchanged
for arg in sys.argv[1:]:
print(getStateOfBoard(arg))