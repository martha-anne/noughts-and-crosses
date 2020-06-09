# Noughts and Crosses

## Brief

### Task
Abiding by the game rules, adapt the Python 3 starting code to calculate the state of a given board. The program should accept boards using the representation in 1.2 as arguments, and should print one result per line in order.

### Board Representation
Boards are represented as strings of length nine, corresponding to the nine slots, starting in the top left slot and counting across each row. The character ”X” is used for Crosses, ”O” (letter O) for Noughts, and ”\_” for empty slots. Note that tests can be any permutation-with-repetition of ”X”, ”O”, and ”\_” of length nine.

### Game Rules
- Crosses always goes first
- Players must make a move during their turn in one of the empty slots
- The game ends as soon as either player gets 3 in a row, or there are no empty slots left

### Starting Code
```
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
```

## Usage

Run main.py from the project root, passing in board definitions:
```python main.py XXXOO____ XX_OOOX__ X_OOO_XXX XXXOXOXOO XOOOXXXXO```

## Testing

Run all discoverable unit tests by running the following command from the project root:
```python -m unittest discover```