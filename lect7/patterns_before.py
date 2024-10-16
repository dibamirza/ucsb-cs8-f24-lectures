# # By the end of this lecture you should be able to complete zyLab 3.14
# # and complete zyLab 3.18 in three different ways

# # Programming patterns involving loops

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


# Problem 2: ZyLab 3.18:Count the number of vowels in a sentence
def countVowels(sentence):
  '''@param sentence is a string
    returns the number of vowels in the string'''
  return 0


user_text = "Listen, Mr. Adams, calm down."

# For the above user_text, your program should print 6 because there are 6 vowels


# Problem 3. Count the number of odd numbers in a list of numbers
def countOddNumber(lst):
  '''@param lst is a list
       returns the number of odd numbers in the lst'''
  return 0



# Problem 4: Return a list with only the positive numbers
def getPositive(lst):
    '''param lst is a list
       return a new list that contains only positive numbers
       in the original lst'''
    '''lst = [ 10, 5, -2, 7]'''
    ''' return  [10, 5, 7]'''
    # one element at a time -> for loop!
    return [42]
