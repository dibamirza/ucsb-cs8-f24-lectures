# Lecture 12: More practice with recursion

def ispalindrome(word):
  '''returns True if the word is a palindrome, otherwise returns False'''
  return False
  
palindromes = ["civic", "kayak", "level", "madam", "mom", "noon", "racecar"]
other = ["minimum", "sardines", "cake", "eeeaowaeee"]
for word in palindromes:
  print(f"{word:12}: {ispalindrome(word)}")

for word in other:
  print(f"{word:12}: {ispalindrome(word)}")

def print_num_pattern(num, step):
  '''@param num is a positive integer
     @param step is a postive integer
     prints a sequence that follows the example pattern
     print_num_pattern(12, 3) prints
     12 9 6 3 0 -3 0 3 6 9 12 
  '''
  pass
