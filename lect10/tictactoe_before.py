# Lecture 10: Demo the process of developing a game (Tic Tac Toe)
# While loops, 5.7 - 5.11 
# List comprehension 5.13
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


board = [['X', '.', 'O'], ['O', '.', '.'], ['.', '.', 'X']]

