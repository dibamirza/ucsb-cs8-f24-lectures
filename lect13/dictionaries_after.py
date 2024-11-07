# Lecture 13: Python Dictionaries - Demo and Practice Problems
# zyBook: 7.1 - 7.3
## Name    | Age
## --------|-----
## Ana     | 3
## Bob     | 2
## Rya     | 5


# What is a dictionary and why use one?
invert_ages = { 'Ana' : 3, 'Bob': 2 , 'Rya': 5}
print(invert_ages)

print("Why use a dictionary? Fast search/lookup + insertion and deletion")



print("\n\nDictionary operations")

# Lookup:
print("Look up Rya's age:", invert_ages['Rya']) # prints 5, look up the value of a key that exists in the dict
#print("Look up Jane's age:", invert_ages['Jane']) # look up the value of a key that doesn't exists in the dict

name = 'Rya'
print(invert_ages[name])

# Search: 
print("Is 'Ana' present in the dictionary?", 'Ana' in invert_ages)
print("Is 'Mark' absent in the dictionary?", 'Mark' not in invert_ages)

# Insert/Update:
invert_ages['Mark'] = 9
print("After adding Mark:", invert_ages)

invert_ages['Bob'] = 9
print("After updating Bob's age:", invert_ages)

# Delete:
del invert_ages['Rya']
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
# Option A: List of tuples
bird_counts_list = [('falcon', 1), ('owl', 5), ('hawk', 2), ('eagle', 11)]

# Option B: Parallell List
kinds = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]

# Option C: Dictionary
bird_data = {'falcon': 1, 'owl': 5, 'hawk': 2, 'eagle': 11}

# Find how many times 'eagle' was seen using each representation
# Option A: List of tuples
bird_counts_list = [('falcon', 1), ('owl', 5), ('hawk', 2), ('eagle', 11)]
bird = 'eagle'
bird = 'hawk'
#bird = 'sparrow'
bird_count = 0
for elem in bird_counts_list:
    # print(type(elem))
    if elem[0] == bird:
        bird_count = elem[1]
print('Eagle count (list of tuples):', bird_count)

# Option B: Parallell List
kinds = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]
bird = 'eagle'
bird = 'hawk'

print('Eagle count (parallel list):', counts[kinds.index(bird)] )
bird = 'hawk'
bird = 'sparrow'
if bird in kinds:
    bird_count = counts[kinds.index(bird)]
else:
    bird_count = 0
    
print('Eagle count (parallel list):', bird_count )
bird_data = {'falcon': 1, 'owl': 5, 'hawk': 2, 'eagle': 11}
bird = 'hawk'

bird = 'eagle'
print("Eagle count (dictionary):", bird_data[bird])
bird = 'sparrow'
print("sparrow count (dictionary):", bird_data.get(bird, 'Not found'))
      


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
kinds = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]
new_data = {}

for elem in kinds:
    new_data[elem] = counts[kinds.index(elem)]

print(new_data)

new_data = {}
for index, bird in enumerate(kinds):
    new_data[bird] = counts[index]

print(new_data)


new_data = {}
for index in range(len(kinds)):
    new_data[kinds[index]] = counts[index]

print(new_data)

data = dict(zip(kinds, counts)) # optional!!
print(data)


bird_counts_list = [('falcon', 1), ('owl', 5), ('hawk', 2), ('eagle', 11)]
print("Converting a list of tuples to a dict")
my_dict = dict(bird_counts_list)
print(my_dict)

# Iterating Over a Dictionary
print("Iterating over elements of a dictionary:")

for key in my_dict: # iterates and only gives keys
    print(key, my_dict[elem])

print("Iterate through key-value pairs")
for key, value in my_dict.items(): # iterates and only gives keys
    print(key, value)
    
## Concept question: Given the dictionary invert_ages,
## what is the most efficient way to find out the age of "Rya"?

my_list = list(my_dict.keys())
print(my_list)

