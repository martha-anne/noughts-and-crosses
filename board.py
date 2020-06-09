import re

class BoardState:
    NOUGHTS_WIN = 'NOUGHTS_WIN'
    CROSSES_WIN = 'CROSSES_WIN'
    DRAW = 'DRAW'
    GAME_IN_PROGRESS = 'GAME_IN_PROGRESS' # This will be used in the case that there is no winner, but empty board spaces remain.
    INVALID = 'INVALID' # This will be used in the case that the numer of Xs is not equal to or one greater than the number of Os.
    # Do we also need to return an INVALID state if we recieve a board where both Xs and Os have formed a line (eg XXXOOO___)? 

class BoardInput:
    CROSS = "X"
    NAUGHT = 'O'
    EMPTY = "_"

class BoardStateDecider:

    

    def __init__(self, board_definition: str):
        self._board_definition_length = 9
        self._re_is_board_definition_supported_length_and_characters = "^[XO_]{" + str(self._board_definition_length) + "}$"
        self._re_is_board_full = "^[XO]{" + str(self._board_definition_length) + "}$"

        self.board_definition = board_definition.upper()

    def decide_state_of_board(self) -> BoardState:

        if not self.__is_board_definition_supported_length_and_characters():
            return BoardState.INVALID
        
        raise Exception("Error")


    def __is_board_definition_supported_length_and_characters(self) -> bool:
        pattern = re.compile(self._re_is_board_definition_supported_length_and_characters)
        return pattern.fullmatch(self.board_definition) is not None

    def __is_board_full(self) -> bool:
        pattern = re.compile(self._re_is_board_full)
        return pattern.fullmatch(self.board_definition) is not None
