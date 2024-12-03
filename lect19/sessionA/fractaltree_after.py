# Lect19 : Fractal trees with turtle
import turtle
import random
jane = turtle.Turtle()
jane.shape("turtle")
jane.width(5)
jane.color("green")
jane.speed(0)
jane.left(90)


def simpleTree(height, branch_len):
    if height == 0:
        jane.forward(branch_len)
##        jane.left(30)
##        jane.forward(branch_len)
##        jane.backward(branch_len)
##        jane.right(60)
##        jane.forward(branch_len)
##        jane.backward(branch_len)
##        jane.left(30)
        jane.backward(branch_len)
        return
    # recursive case
    jane.forward(branch_len)
    jane.left(30)
    simpleTree(height-1, branch_len)
    jane.right(60)
    simpleTree(height-1, branch_len)
    jane.left(30)
    jane.backward(branch_len)
    

def fancyTree(height, branch_len, pen_width):
    if height == 0:
        jane.forward(branch_len)
        jane.backward(branch_len)
        return
    # recursive case
    if pen_width > 1:
        pen_width = pen_width - 1
    jane.width(pen_width)
    branch_len = branch_len * random.randint(7, 9)/10
    left_turn = random.randint(30, 50)
    right_turn = random.randint(30, 50)
    jane.forward(branch_len)
    jane.left(left_turn)
    fancyTree(height-1, branch_len, pen_width)
    jane.right(left_turn+right_turn)
    fancyTree(height-1, branch_len, pen_width)
    jane.left(right_turn)
    jane.backward(branch_len)

    
    
    
jane.up()
jane.backward(100)
jane.down()
fancyTree(6, 100, 10)
                
    
