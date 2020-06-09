import re

class BoardState:
    NOUGHTS_WIN = 'NOUGHTS_WIN'
    CROSSES_WIN = 'CROSSES_WIN'
    DRAW = 'DRAW'
    # GAME_IN_PROGRESS be used in the case that there is no winner, but empty board spaces remain.
    GAME_IN_PROGRESS = 'GAME_IN_PROGRESS'
    # INVALID will be used in the case that the numer of Xs is not equal to or one greater than the number of Os, indicating unnatural gameplay.
    # INVALID will also be used if we recieve a board where both Xs and Os have formed a line (eg XXXOOO___), as this also indicated unnatural gameplay. 
    INVALID = 'INVALID' 

class BoardInput:
    CROSS = "X"
    NOUGHT = 'O'
    EMPTY = "_"

class BoardStateDecider:

    # Regex to check for a string of length 9 containing only the characters X O and _.
    _re_is_board_definition_supported_length_and_characters = "^[XO_]{9}$" 

    # Regex to check for a string of length 9 containing only the characters X and O.
    _re_is_board_full = "^[XO]{9}$"

    # Indexes of the board definition corresponding to horizontal, vertical or diagonal lines.
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
        # Cast the board definition to uppercase. All checks from now on will assume uppercase characters.
        self.board_definition = board_definition.upper()

    def decide_state_of_board(self) -> BoardState:

        # Check that the board definition is 9 characters long, and contains only X O and _. Return invalid if not.
        if not self.__is_board_definition_supported_length_and_characters():
            return BoardState.INVALID
        
        # Check that the board does not have an excessive number of Xs or Os so as to indicate unnatural gameplay. Return invalid if not.
        if not self.__is_board_definition_natural_gameplay():
            return BoardState.INVALID

        # Check whether noughts and crosses have managed to successfully make lines
        board_has_lines = self.__get_board_has_lines()
        noughts_has_line = board_has_lines[BoardInput.NOUGHT]
        crosses_has_line = board_has_lines[BoardInput.CROSS]

        # If both noughts and crosses have made a line, gameplay has been unnatural. Return invalid.
        if noughts_has_line and crosses_has_line:
            return BoardState.INVALID

        # If only noughts or only crosses has made a line, that party is considered to have won. Return winner.
        if noughts_has_line:
            return BoardState.NOUGHTS_WIN

        if crosses_has_line:
            return BoardState.CROSSES_WIN
        
        # If the board is full, there have been no winners, and no valid moves remain, return draw.
        if self.__is_board_full():
            return BoardState.DRAW

        # In all other cases we can consider the game to remain in progress.
        return BoardState.GAME_IN_PROGRESS


    def __is_board_definition_supported_length_and_characters(self) -> bool:
        pattern = re.compile(self._re_is_board_definition_supported_length_and_characters)
        return pattern.fullmatch(self.board_definition) is not None

    def __is_board_definition_natural_gameplay(self) -> bool:
        crosses_count = self.board_definition.count(BoardInput.CROSS)
        noughts_count = self.board_definition.count(BoardInput.NOUGHT)

        return crosses_count == noughts_count or crosses_count == (noughts_count + 1)

    def __is_board_full(self) -> bool:
        pattern = re.compile(self._re_is_board_full)
        return pattern.fullmatch(self.board_definition) is not None

    def __get_board_has_lines (self) -> dict:
        board_has_lines = {
            BoardInput.CROSS: False,
            BoardInput.NOUGHT: False
        }

        for line_index_definition in self._line_index_definitions:
            if self.__board_has_line(BoardInput.CROSS, line_index_definition):
                board_has_lines[BoardInput.CROSS] = True
            elif self.__board_has_line(BoardInput.NOUGHT, line_index_definition):
                board_has_lines[BoardInput.NOUGHT] = True

            if board_has_lines[BoardInput.CROSS] and board_has_lines[BoardInput.NOUGHT]:
                break
        
        return board_has_lines

    def __board_has_line(self, board_input: BoardInput, line_index_definition: list) -> bool:
        line = self.board_definition[line_index_definition[0]] + self.board_definition[line_index_definition[1]] + self.board_definition[line_index_definition[2]] 
        return line == board_input * 3
        

