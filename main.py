import sys

import board

# complete this function so that it returns the correct board state
def getStateOfBoard(board_definition: str) -> board.BoardState:
    board_state_decider = board.BoardStateDecider(board_definition)
    return board_state_decider.decide_state_of_board()

# leave this part unchanged
for arg in sys.argv[1:]:
    print(getStateOfBoard(arg))