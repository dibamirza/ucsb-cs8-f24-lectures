# Lecture 9: Tic Tac Toe
# How do we represet the different things 
# that make up a game
matrix = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9] ]
print(matrix[0]) # row 0
print(matrix[1]) # row 1
print(matrix[2]) # row 2
print(matrix[1][1])
print(matrix[2][1]) # prints 8 
matrix[2][1] = 80
print(matrix[2][1]) # prints
def print_board_v0(board):
  ''' input board is a nested list
    prints the board in the following format
     X | . | O 
    ---+---+---
     O | . | .  
    ---+---+---
     . | . | X 
  '''
  for row in board:
    print(f" {row[0]} | {row[1]} | {row[2]}")
    print("---+---+---")
  return

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
# Weigh the pros an cons
board1 = "X.O\nO..\n..X" # Con: strings are immutable, difficult to update the board
print(board1)
board2 = " X | . | O \n"\
         "---+---+---\n"\
         " O | . | . \n"\
         "---+---+---\n"\
         " . | . | X \n" 
print(board2) # Pro: Its easier to print the board
lboard = ['X', '.', 'O', 'O', '.', '.', '.', '.', 'X']
print("Board before update")
print(lboard) 
print("Board after update")
lboard[4] = 'X' # need a formula to go from row_index, col_index -> index in list
print(lboard) # Pro: lists are mutable, updates are easier
xboard = [['X', '.', 'O'], ['O', '.', '.'], ['.', '.', 'X']]

print("Board before update")
print_board(xboard) 
print("Board after update")
xboard[1][1] = 'X' # need a formula to go from row_index, col_index -> index in list
print_board(xboard)
# Nested lists

# Three ways of solving the fencepost problem
# Method 1 will not work if the list has duplicates
# print("Method 1")
nums = [10, 20 , 30]
for elem in nums:
  print(elem, end = "")
  if not (elem  == nums[-1]):
    print("-", end = "")
print()

# print("Method 2")
for i in range(len(nums)):
  print(nums[i], end = "")
  if i < len(nums) - 1:
    print("-", end = "")
print()

# Method 3
for (i, elem) in enumerate(nums):
  print(elem, end = "")
  if i < len(nums) - 1:
    print("-", end = "")

