# fizzbuzz.py
# Author: Diba Mirza
# Lecture 4: Functions with branching
# Zybook 2.5, 2.8 – 2.11, 2.19

# Demo: How to incrementally develop code

# Write the stub of the function
def fizzbuzz(num):
    ''' int -> str
    returns "Fizz" if the num is divisible by 3
            "Buzz" if the num is divisible by 5
            "Fizzbuzz" if the num is divisible by both 3 and 5
            str(num), in all other cases
    '''
    if (num % 3 == 0 and num % 5 == 0):
        return "Fizzbuzz" # return statement marks the end of the function
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


print(f"{fizzbuzz(15)=}")
print(f"{fizzbuzz(9)=}")
print(f"{fizzbuzz(5)=}")
print(f"{fizzbuzz(42)=}")
print(f"{fizzbuzz(1)=}")

