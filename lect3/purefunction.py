# examples of pure and not pure functions
# Pure function: depends only on input
def add(x, y):
    return x + y


#Not Pure: If a function modifies external state or has side effects, it is not considered pure.

total = 0  # external state

def add_to_total(x):
    global total
    total += x  # modifies external state (side effect)

