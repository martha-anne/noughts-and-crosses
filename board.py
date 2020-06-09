import re
from enum import Enum

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

    _re_is_board_definition_supported_length_and_characters = "^[XO_]{9}$"
    _re_is_board_full = "^[XO]{9}$"
    _line_index_definitions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self, board_definition: str):
        self.board_definition = board_definition.upper()

    def decide_state_of_board(self) -> BoardState:

        if not self.__is_board_definition_supported_length_and_characters():
            return BoardState.INVALID
        
        if not self.__is_board_definition_natural_gameplay():
            return BoardState.INVALID

        noughts_has_line = self.__board_has_any_line(BoardInput.NAUGHT)
        crosses_has_line = self.__board_has_any_line(BoardInput.CROSS)

        if noughts_has_line and crosses_has_line:
            return BoardState.INVALID

        if noughts_has_line:
            return BoardState.NOUGHTS_WIN

        if crosses_has_line:
            return BoardState.CROSSES_WIN
        
        if self.__is_board_full():
            return BoardState.DRAW

        return BoardState.GAME_IN_PROGRESS


    def __is_board_definition_supported_length_and_characters(self) -> bool:
        pattern = re.compile(self._re_is_board_definition_supported_length_and_characters)
        return pattern.fullmatch(self.board_definition) is not None

    def __is_board_definition_natural_gameplay(self) -> bool:
        crosses_count = self.board_definition.count(BoardInput.NAUGHT)
        noughts_count = self.board_definition.count(BoardInput.NAUGHT)

        return crosses_count == noughts_count or crosses_count == (noughts_count + 1)

    def __is_board_full(self) -> bool:
        pattern = re.compile(self._re_is_board_full)
        return pattern.fullmatch(self.board_definition) is not None

    def __board_has_any_line(self, board_input: BoardInput) -> bool:
        for line_index_definition in self._line_index_definitions:
            if self.__board_has_line(board_input, line_index_definition):
                return True   
        return False

    def __board_has_line(self, board_input: BoardInput, line_index_definition: list) -> bool:
        line = self.board_definition[line_index_definition[0]] + self.board_definition[line_index_definition[1]] + self.board_definition[line_index_definition[2]] 
        return line == board_input * 3
        

