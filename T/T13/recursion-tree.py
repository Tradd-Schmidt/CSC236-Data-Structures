#-------------------------------------------------------------------------------
# Purpose:  Recursive tree
#-------------------------------------------------------------------------------

import turtle
import random


def tree(branchLen, t, size, angle):
    """
    Draws a tree with using recursive calls
    :param branchLen: The length of a branch to be drawn
    :param t: A turtle
    :return: none
    """
    if branchLen > 5:
        t.pensize(size)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-random.randint(5, 15), t, size - 2, random.randint(15, 60))
        t.left(angle*2)
        tree(branchLen-random.randint(5, 15), t, size - 2, random.randint(15, 60))
        t.right(angle)
        t.backward(branchLen)


def main():
    """
    Sets up the positioning to draw a tree using a turtle and the recursive function tree()
    :return: none
    """
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t, 25, random.randint(15, 60))
    myWin.exitonclick()

main()
