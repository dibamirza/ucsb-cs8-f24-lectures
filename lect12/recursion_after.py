# Lecture 12: More practice with recursion

def ispalindrome(word):
  '''returns True if the word is a palindrome, otherwise returns False'''
  if len(word) == 0:
    return True
  if len(word) == 1:
    return True
  if len(word) == 2:
    return word[0] == word[-1]
  if len(word) == 3:
    return word[0] == word[-1]

  if word[0] == word[-1]:
    return ispalindrome(word[1:-1])
  else:
    return False
  
palindromes = ["civic", "kayak", "level", "madam", "mom", "noon", "racecar"]
other = ["minimum", "sardines", "cake", "eeeaowaeee"]
print("Palindromes")
for word in palindromes:
  print(f"{word:12}: {ispalindrome(word)}")

print("Non-palindromes")
for word in other:
  print(f"{word:12}: {ispalindrome(word)}")

def print_num_pattern(num, step):
  '''@param num is a positive integer
     @param step is a postive integer
     prints a sequence that follows the example pattern
     print_num_pattern(12, 3) prints
     12 9 6 3 0 -3 0 3 6 9 12 
  '''
  # Base case
  if _______:
    print("a number", end = " ")
    print("another number", end = " ")
    print("the last number", end = " ")
    return
  
  pass












