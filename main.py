import sys

# complete this enum with all the possible states of a noughts and crosses board (there's more than 3)
class BoardState:
NOUGHTS_WIN = 'NOUGHTS_WIN'
CROSSES_WIN = 'CROSSES_WIN'
DRAW = 'DRAW'

# complete this function so that it returns the correct board state
def getStateOfBoard(board):
return BoardState.DRAW

# leave this part unchanged
for arg in sys.argv[1:]:
print(getStateOfBoard(arg))