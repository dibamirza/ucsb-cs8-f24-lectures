# Nested Loops, practice problems with ASCII Art
# # 1. Draw a rectangle, given its width and height
# # 2. Draw the letter C, given its width and height

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
# print(getRectangle(4, 5))
# print(getRectangle(10, 5))



# 2. Write a function that returns a string representing the letter C, given its width and height
def getC(width, height):
    '''returns a string representing the letter C 
        using *s with given width and height'''
    return ""
