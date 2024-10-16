# Lecture 6: Test Driven Development
# Different ways of running a python program
# In IDLE: (Function F5) F5
# Zybook: python3 <name of the file>

# Problem: "Triangle Type Checker"
# Problem Statement:
# Write a program that determines the type of a triangle
# (Equilateral, Isosceles, or Scalene) based on the lengths of its sides. 
# The program should also check whether the three sides can actually 
# form a valid triangle using the Triangle Inequality Theorem
# (sum of any two sides of a triangle must be greater than the third side).


# How do I get started?
# Step 1 : Figure input - output
# What are the inputs and what are the outputs?
# Inputs: 3 numbers, Output: Invalid, Equilateral, Isosceles, or Scalene


# Step 2: Problem decomposition
# Sub problem 1: check if its a valid triangle
# Sub problem 2: get the type of the triangle

# 2a: Write the stub of the functions
def is_valid_triangle(a, b, c):
    ''' float, float, float -> bool
    inputs must be positive
    checks if a triangle is valid:
    sum of any two sides of a triangle must be greater than the third side
    '''

    return (a + b) > c and (b + c) > a and (c + a) > b

##    if (a + b) > c and (b + c) > a and (c + a) > b:
##        return True
##    
##    return False

def get_triangle_type(a, b, c):
    ''' float, float, float -> str
    returns one of three possible types:
    "Equilateral", "Isosceles", or "Scalene"
    '''
    if a == b and b== c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# print(__name__) # When we run triangle.py directly
# __name__ gets the value "__main__"

if __name__ == "__main__":
    x = float(input("Enter the first side: "))
    y = float(input("Enter the second side: "))
    z = float(input("Enter the third side: "))

    if not is_valid_triangle(x, y, z):
        print("Not a valid triangle")
    else:
        print(f"Triangle is type: {get_triangle_type(x, y, z)}")








