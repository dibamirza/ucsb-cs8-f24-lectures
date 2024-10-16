# # Lecture 7 : Loops and functons 3.8, 4.1 - 4.11
# # By the end of this lecture you should be able to complete
# # zyLabs 4.5 (leap year functions),
# # zyLabs 4.6(range withincrements of 5),
# # zyLabs 4.8 (count vowels) and 4.11 (password modifier)

# # You should also be able to complete 4.8 and
# # similar labs in three different ways

# # Problem 1: Write your own implementation of Python's sum function
def mysum(lst):
  '''param lst is a list
       returns the sum of the elements in the lst'''
  return 0


l1 = [1, 5, 7]
l2 = [1, 5, 7, 10]
l3 = [1] * 10
print(f"mysum({l1}) expected: {sum(l1)}, actual = {mysum(l1)}")
print(f"mysum({l2}) expected: {sum(l2)}, actual = {mysum(l2)}")
print(f"mysum({l3}) expected: {sum(l3)}, actual = {mysum(l3)}")


# Problem 2: Write a program to remove all the vowels in a string
def removeVowels(sentence):
  '''@param sentence is a string
  complete the docstring'''
  return 0


input_text = "Listen, Mr. Adams, calm down."
expected_text = "Lstn, Mr. dms, clm dwn."

# Problem 3: Return a list with only the positive numbers
def getPositive(lst):
    '''param lst is a list
       return a new list that contains only positive numbers
       in the original lst'''
    '''lst = [ 10, 5, -2, 7]'''
    ''' return  [10, 5, 7]'''
    return [42]


# Problem 4. Count the number of odd numbers in a list of numbers
def countOddNumber(lst):
  '''@param lst is a list
       returns the number of odd numbers in the lst'''
  return 0

# Problem 5: Check for any odd numbers
def containsOddNumber(lst):
  '''return True if any element in lst is odd,
     otherwise return False'''
  return True

## Discuss the range function of python

# Problem 6: Sum every other element
def sum_every_second_element(numbers):
  '''returns the sum of every other element in a list'''
        
  return 0

# Test the function
numbers = [5, 8, 12, 20, 7, 15, 3, 10]
actual = sum_every_second_element(numbers)
print("Sum of every second element:", f"{actual= }")


