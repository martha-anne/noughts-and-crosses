class BoardState:
    NOUGHTS_WIN = 'NOUGHTS_WIN'
    CROSSES_WIN = 'CROSSES_WIN'
    DRAW = 'DRAW'
    GAME_IN_PROGRESS = 'GAME_IN_PROGRESS' # This will be used in the case that there is no winner, but empty board spaces remain.
    INVALID = 'INVALID' # This will be used in the case that the numer of Xs is not equal to or one greater than the number of Os.
    # Do we also need to return an INVALID state if we recieve a board where both Xs and Os have formed a line (eg XXXOOO___)? 

class BoardStateDecider:

    def __init__(self, board_definition: str):
        # Assign the argument to the instance's name attribute
        self.board_definition = board_definition

    def decide_state_of_board(self) -> BoardState:
        return BoardState.INVALID