# Lecture 4: Functions and branching
# What is the difference between print vs return
# inside an if block? 
# note: return statements can only be included
# inside functions

def foo(x):
    if x > 3:
        print("Hello")
    print("Goodbye")

def bar(x):
    if x > 3:
        return "Hello"
    print("Goodbye")

foo(5)       #prints both "Hello" and "Goodbye"
print(bar(5))# prints only "Hello", return ends function execution
foo(1)       # prints only "Goodbye" (if cond is False)
bar(1)       # prints only "Goodbye" (if cond is False)


##if x < 0:
##    print(f"{x} is negative")
##elif x == 0:
##    print(f"{x} is zero")
##else:
##    print(f"{x} is positive")
##
##print("Bye")
##
##
