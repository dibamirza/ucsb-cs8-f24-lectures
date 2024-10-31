# Lecture 11: Recursion, zybook 6.1 - 6.3
# What is recursion and why is it important in CS?

# Review of function calling another function
def happy(message):
    print(message)

def sing(P, msg):
    happy(msg)
    happy(msg)
    print("Happy Birthday dear " + P + "!")
    happy(msg)

# main
sing("Fred", "Happy Birthday to you!")

# What is the output?

# A. Happy Birthday to you!

# B. Happy Birthday dear Fred!

# C. Happy Birthday to you!
#    Happy  Birthday to you!

# D. Happy Birthday to you!
#    Happy  Birthday to you!
#    Happy Birthday dear Fred!
#    Happy Birthday to you!

# E. Error: cannot call happy() function inside sing() function


#zybook CA 6.1.1
# Write a statement that calls the recursive function backwards_alphabet() with input starting_letter.
def backwards_alphabet(curr_letter):
    if curr_letter == 'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input()


def fac(n):
    """
    returns the factorial of n
    """
    pass

#zybook PA 6.1
def countDown(n):
    ''' print values n n-1 n-2 ... 1 Go!
        n = 3
        print 3 2 1 Go!
    '''

def sumListRecursive(lst):
    ''' :param lst is a list containing integer values
        returns the sum of the elements in a list lst'''
    '''lst: [ 1, 2, 3, 5] returns 11'''
    
    # Writing the base case
    # 1. What is the simplest input?
  
    # 2. What should the result be for the simplest input?
  
    # Write the recursive description

    return 42

# sumListRecursive([10]) 


# sumListRecursive([10, 20])


# sumListRecursive([50, 10, 20])

    

##print("sumListRecursive([]):", sumListRecursive([]))
##print("sumListRecursive([10]):", sumListRecursive([10]))
##print("sumListRecursive([100]):", sumListRecursive([100]))
##print("sumListRecursive([200]):", sumListRecursive([200]))
##print("sumListRecursive([10, 20]):", sumListRecursive([10, 20]))
## print("sumListRecursive([50, 10, 20]):", sumListRecursive([50, 10, 20]))


# Approach for an iterative solution that uses loops is quite different
def sumListIterative(lst):
    ''' :param lst is a list containing integer values
        returns the sum of the elements in a list lst'''
    '''lst: [ 1, 2, 3, 5] return 11'''
    result = 0
    for elem in lst:
        result+=elem
    return result


def ispalindrome(word):
  '''returns True if the word is a palindrome, otherwise returns False'''
  return False
  
palindromes = ["civic", "kayak", "level", "madam", "mom", "noon", "racecar"]
other = ["minimum", "sardines", "cake", "eeeaowaeee"]
for word in palindromes:
  print(f"{word:12}: {ispalindrome(word)}")

for word in other:
  print(f"{word:12}: {ispalindrome(word)}")



    
    

