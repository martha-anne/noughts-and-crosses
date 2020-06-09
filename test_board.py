import unittest

import board

class TestBoardStateDecider(unittest.TestCase):

    def test_decide_state_of_board_expect_invalid_when_board_definition_has_unsupported_characters (self):
        board_definition = "1234KKXXX"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.INVALID)

    def test_decide_state_of_board_expect_invalid_when_board_definition_is_not_9_characters (self):
        board_definition = "XXXOO_"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.INVALID)
    
    def test_decide_state_of_board_expect_invalid_when_board_definition_has_multiple_winners (self):
        board_definition = "XXXOOO___"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.INVALID)

    def test_decide_state_of_board_expect_invalid_when_board_definition_has_too_many_xs (self):
        board_definition = "XXXXXOOO_"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.INVALID)

    def test_decide_state_of_board_expect_invalid_when_board_definition_has_too_many_os (self):
        board_definition = "OOX______"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.INVALID)

    def test_decide_state_of_board_expect_game_in_progress_when_board_definition_has_empty_spaces_and_no_winner (self):
        board_definition = "OOXXOO___"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.GAME_IN_PROGRESS)

    def test_decide_state_of_board_expect_draw_when_board_definition_has_no_empty_spaces_and_no_winner (self):
        board_definition = "OOXXXOOOX"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.DRAW)

    def test_decide_state_of_board_expect_crosses_win_when_board_definition_has_horizontal_line (self):
        board_definition = "OO_XXX___"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.CROSSES_WIN)

    def test_decide_state_of_board_expect_crosses_win_when_board_definition_has_vertical_line (self):
        board_definition = "XO_XO_X__"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.CROSSES_WIN)

    def test_decide_state_of_board_expect_crosses_win_when_board_definition_has_diagonal_line (self):
        board_definition = "OOX_X_X__"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.CROSSES_WIN)

    def test_decide_state_of_board_expect_noughts_win_when_board_definition_has_horizontal_line (self):
        board_definition = "X___XXOOO"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.NOUGHTS_WIN)

    def test_decide_state_of_board_expect_noughts_win_when_board_definition_has_vertical_line (self):
        board_definition = "X_OXXO__O"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.NOUGHTS_WIN)

    def test_decide_state_of_board_expect_noughts_win_when_board_definition_has_diagonal_line (self):
        board_definition = "OXX_O__XO"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.NOUGHTS_WIN)

    def test_decide_state_of_board_expect_correct_behaviour_when_board_definition_is_lowercase (self): 
        board_definition = "xxxoo____"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.CROSSES_WIN)

    def test_decide_state_of_board_expect_crosses_win_when_board_definition_has_no_empty_spaces_and_horizontal_line (self):
        board_definition = "OXOXOXXXX"
        board_state_decider = board.BoardStateDecider(board_definition)
        self.assertEqual(board_state_decider.decide_state_of_board(), board.BoardState.CROSSES_WIN)

if __name__ == '__main__':
    unittest.main()