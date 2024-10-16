# Lecture 6: Sequences

# Types in Python
# bool, int, float, string
# String: sequence of characters "apple"
# Today: list another type of sequence of any type
# Why do we need new types to store sequences


# Ordered Sequences
# strings are a sequence of characters  "spam"
food = 'spam'
# Lists" ordered sequence of any type  
grocery = ['spam', 'milk', 'eggs', 'apple']
student = ["Jane Doe", "A327838394", 3.3]

# why do we need lists?

item1 = 'spam'
item2 = 'milk'
item3 = 'eggs'
item4 = 'apple'

# The trouble with not using lists is that we need to come up with different variables to store each thing

# Once you have a list you can index into it to get the individual elements
name = student[0]
perm = student[1]
gpa = student[2]

# The index is just a number (only integers allowed)
# for the position of the value
# Since lists and strings are ordered, there is a notion of
# position of each element: first element is at index 0,
# second element is at index 1, and so on

# Index vs Value

print(food[0])
print(food[1])
print(food[-1])

# >>> food[-6]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# Beware of providing an index that is out of range

# List: we can change the value of any element 
grocery[0] = 'flour'
stu = ('John', 'Doe', "A384387437484")
# cannot change the individual elemens of the tuple
# stu[0] = 'Diba': give us an error 


cone_snails = ["purple", "blue", "green"]
print(cone_snails[1])
print(cone_snails[1] == "orange")
cone_snails[1] = "orange"
print(cone_snails)


# Passing lists to functions
def scared(eel_param):
  eel_param[1] = 'checkerboard'


eel = ['dots', 'stripes', 'swirls']
scared (eel)
print(eel) # prints 
 ['dots', 'checkerboard', 'swirls']
# What is interesting in this example is that the scared function
# changed the input list and the effect was seen outside the function
# Stated differently, the function produced an ouput without returning
# anything. This is the first time we have seen a function do that
# In class we discussed the mechanics of how lists are passed into functions
# by default which explains the above behavior

same_eel = eel # Although same_eel is a different variable it points to the same list object as eel
               # changing one will change the other
twin = eel[:]  # makes a copy of the entire list

# So if you don't want the scared function to be able to modify the original input
# Call it on a copy of the list

eel = ['dots', 'stripes', 'swirls']
scared (eel[:])
print(eel) # the original eel is unaffected
