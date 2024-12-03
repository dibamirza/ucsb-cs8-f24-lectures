# Lect19 : Fractal trees with turtle
import turtle
import random
jane = turtle.Turtle()
jane.shape("turtle")
jane.width(5)
jane.color("green")
jane.speed(0)
jane.left(90)
# Drawing a simple height 1 tree


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
    jane.forward(branch_len)
    jane.left(30)
    simpleTree(height - 1, branch_len)
    jane.right(60)
    simpleTree(height - 1, branch_len)
    jane.left(30)
    jane.backward(branch_len)


def fancyTree(height, branch_len, pen_width):
    if height == 0:
        jane.forward(branch_len)
        jane.backward(branch_len)
        return
    branch_len = branch_len * random.randint(7, 9)/10
    left_turn = random.randint(20, 50)
    right_turn = random.randint(20, 50)
    if pen_width > 1:
        pen_width = pen_width - 1

    jane.width(pen_width)
    jane.forward(branch_len)
    jane.left(left_turn)
    fancyTree(height - 1, branch_len, pen_width)
    jane.right(left_turn + right_turn )
    fancyTree(height - 1, branch_len, pen_width)
    jane.left(right_turn)
    jane.backward(branch_len)



    
jane.up()
jane.backward(200)
jane.down()
fancyTree(10, 80, 8)
    
