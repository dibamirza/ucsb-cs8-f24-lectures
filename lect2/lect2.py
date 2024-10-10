# Lecture 2: Data types, variables, programs that take input and produce output!
# Personalized message
user_name = input("Enter your name: ")
print("Hello", user_name, "!")
print(f"Hello {2*2} World!")
print(f"Hello {user_name}!")
print(f"{2*2=}")
x = float(input ("Enter a number: "))
print(f"Double of {x} is {2*x}")
speed_of_light = 3 * 10 ** 8 # m/s
distance_to_sun = 149597870700 # meters
time = distance_to_sun/speed_of_light/60
print(f"It takes {time:0.2f} mins for light to reach the earth from the sun")
