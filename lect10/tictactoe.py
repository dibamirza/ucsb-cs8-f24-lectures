# Lecture 10: Demo the process of developing a game (Tic Tac Toe)
# While loops, 5.7 - 5.11 
# List comprehension 5.13

# Pseudocode for the game
# Initialize an empty board
# Select player 1 and player 2 
# Select current player
# Repeat these steps until the game is over:
#  print the board
#  Get the current player's move
#. Update the board
#  Check the status of the board
#  If any player wins or if it is a draw, then end the game
#. Else switch players
# Print the result of the game
def print_board(board):
  ''' input board is a nested list
    prints the board in the following format
     X | . | O 
    ---+---+---
     O | . | .  
    ---+---+---
     . | . | X 
  '''
  for (i, row) in enumerate(board):
    print(f" {row[0]} | {row[1]} | {row[2]}")
    if i < 2:
      print("---+---+---")
  return

def update_board(board, player, move):
    ''' update the board with player's move
    @param board: nested list
    @param player: string 'X' or 'O'
    @param move:  tuple (row, col)
    '''
    row_index = move[0]
    col_index = move[1]
    board[row_index][col_index] = player
    return 

def check_status(board):
    '''return 'win', 'draw', or  'go' depending on the status'''
    return 'go'

def play():
    board = [['X', '.', 'O'], ['O', '.', '.'], ['.', '.', 'X']]
    # Identify how to represent different things in our game
    # board: nested list
    # player: string 'X' or 'O'
    # move: tuple (row, col)   pos on the board 
    # state of the game: bool

    # Initialize an empty board
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    # Select player 1 and player 2 
    # Select current player
    current_player = 'X'
    # Repeat these steps until the game is over:--> set up a loop
    game_over = False
    while not game_over:
        # Repeat these steps
        #  print the board
        print_board(board)
        #  Get the current player's move
        move = input(f"Player {current_player} enter your move (row, col): ")
        # move is a str and not a tuple --- fix this
        # move = "0, 1"
        lst_move = move.split(",")
        # print(lst_move)
        # ['0', '1']
        tuple_move = (int(lst_move[0]), int(lst_move[1]))
        # print(tuple_move)
        #. Update the board
        update_board(board, current_player, tuple_move)
        #  Check the status of the board
        status = check_status(board) # 'win' , 'draw', or 'go'
        #  If any player wins or if it is a draw, then end the game
        #. Else switch players
        if status == 'win' or status == 'draw':
            game_over = True
        else: 
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

    # Print the result of the game
    print(status)

# play()
# initializing the board: Method 1 : '*' repetion operator
row = ['.'] * 3
print(row)
# board = [row]* 3
# print_board(board)
# board[0][1] ='X'
# print_board(board)

print("Method 2: accumulator pattern")
# method 2: for loop accumulator pattern
board = []
for i in range(3):
    board.append(row[:])

board[1][0] ='X'
print_board(board)

# Method 3: List comprehensionn 5.13
# Next lecture




