# Lecture 13: Python Dictionaries - Demo and Practice Problems
# zyBook: 7.1 - 7.3
## Name    | Age
## --------|-----
## Ana     | 3
## Bob     | 2
## Rya     | 5


# What is a dictionary and why use one?
invert_ages = { 'Ana' : 3, 'Bob': 2 , 'Rya': 5}

print("Why use a dictionary?")
print("\n\nDictionary operations")

# Lookup:
print("Rya's age:")

# Search: 
print("Is 'Ana' present in the dictionary?")
print("Is 'Mark' absent in the dictionary?")

# Insert: 
print("After adding Mark:", invert_ages)

# Update:
print("After updating Bob's age:", invert_ages)

# Delete:
print("After deleting an element:", invert_ages)


## Which of the following is best suited for a dictionary instead of a list?
##  A. The order in which people finish a race. 
##  B. The ingredients necessary for a recipe
##  C. The names of world countries and their capital cities
##  D. 50 random integers

print("\n\n")
# Example: Given a list of bird species and their respective counts,
# find the count of a given bird
##+---------+-------+
##| Bird    | Count |
##+---------+-------+
##| falcon  |     1 |
##| owl     |     5 |
##| hawk    |     2 |
##| eagle   |    11 |
##+---------+-------+

# What are some possible ways we can represent the above data?
# Option A: 
bird_counts_list = [('falcon', 1), ('owl', 5), ('hawk', 2), ('eagle', 11)]

# Option B:
kinds = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]

# Option C: 

# Find how many times 'eagle' was seen using each representation
        
print('Eagle count (list of tuples)')

print('Eagle count (parallel list)')

print("Eagle count (dictionary):")
      


# Problem: Update Parallel Lists Using a Dictionary
def new_sighting(kinds, counts, sighting):
    '''
    @param kinds is a list of strings (bird names)
    @param counts is a list of integers (count of each bird)
    @param sighting is a string (a bird that was sighted)
    Update the parallel lists `kinds` and `counts` to add the new sighting.
    '''
    if sighting not in kinds:
        kinds.append(sighting)
        # … missing code
    
    ind = kinds.index(sighting)
    counts[ind] += 1

kinds = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]
new_sighting(kinds, counts, 'owl')
print("Kinds after new sighting:", kinds)
print("Counts after new sighting:", counts)


# Transform parallel lists into a dictionary


# Iterating Over a Dictionary
print("Iterating over elements of a dictionary:")

## Concept question: Given the dictionary invert_ages,
## what is the most efficient way to find out the age of "Rya"?



