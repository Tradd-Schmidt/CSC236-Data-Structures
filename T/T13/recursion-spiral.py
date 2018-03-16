#-------------------------------------------------------------------------------
# Purpose:  Recursive spiral
#-------------------------------------------------------------------------------

import turtle


def drawSpiral(myTurtle, lineLen):
    """
    Draws a line and turns right until the length of the line is less than or equal to 0
    :param myTurtle: A turtle
    :param lineLen: The length of the line to be drawn
    :return: none
    """
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)


def main():
    """
    Creates a turtle and a turtle screen. Then calls the drawSpiral() function.
    :return: none
    """
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    drawSpiral(myTurtle,100)
    myWin.exitonclick()

main()
