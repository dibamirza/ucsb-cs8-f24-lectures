# Lecture 3: Functions

# Main questions
# How to create a function? By defining it
# How to use a function? By calling it

# Area of a circle
import math
# To make a function: define the function
def area_of_circle(radius):
    # Body of the function
    '''@param radius: float
       returns the area of the circle with the given radius'''
    # local variable: variable that is created inside a function
    result = math.pi * radius ** 2
    return result


# print(result) # Error because result is a local variable
# To use the function: call the function
x = area_of_circle(10)
print(f"{area_of_circle(2)= :0.2f}")


name = "Joe"
def greeting():
    print(f"Welcome {name}")
    return  # returning None value


def greeting_v1(pname):
    print(f"Welcome {pname}")
    return  # returning None value
    


greeting()
greeting_v1("Diba")
greeting_v1("Jane")
greeting_v1("Joe")



def f(x):
    return 2*x

def g(x):
    print(2*x)


print(f(32)) # prints the return value of f(32), which is 64
print(g(32)) # prints the return value of g(32), which is None

