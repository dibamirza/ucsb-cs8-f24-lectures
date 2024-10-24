# Nested Loops, practice problems with ASCII Art
# # 1. Draw a rectangle, given its width and height
# # 2. Draw the letter C, given its width and height

# Review of the accumulator pattern

def message():
    '''What does this function return?'''
    sentence_list = ['Hello', 
                     'fellow coder!',
                     'Remember to take short breaks when coding!']
    result = ""
    for elem in sentence_list:
        result += elem + "\n"
    
    return result

print(message())

# 1. Write a function that returns a rectangle of *'s', given its width and height
def getRectangle(width, height):
  '''returns a string representing a 
     rectangle of *s with given width and height'''
  return ""


print(getRectangle(3, 4))



# 2. Write a function that returns a string representing the letter C, given its width and height
def getC(width, height):
  '''returns a string representing the letter C 
     using *s with given width and height'''
  pass

# Let's use the AI tutor duck to understand the purpose of this nested loop
# Prompt: Explain what this code is doing.
for i in range(2):
   for j in range(3):
      print(i, j)
# Prompt: Can you explain with an example how the above code can be useful to draw the letter C using stars and spaces?
