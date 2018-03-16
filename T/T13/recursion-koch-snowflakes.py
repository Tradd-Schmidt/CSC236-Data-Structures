'''
Koch curve code modified  by Dr. Jan Paarce
from http://openbookproject.net/thinkcs/python/english3e/recursion.html
'''

import turtle
import random

class Koch:
    def __init__(self, order=3, size=200):
        self.order = order
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.color("pink")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(-1*size//2, size//2)
        self.turtle.pendown()

    def draw_koch(self, t, neworder, newsize):
        if neworder == 0:
            t.forward(newsize)
        else:
            for angle in [60, -120, 60, 0]:
                self.draw_koch(t, neworder-1, newsize//3)
                t.left(angle)

    def snowflake(self):
        for i in range(3):
            self.draw_koch(self.turtle, self.order, self.size)
            self.turtle.right(120)

def main():
    wn=turtle.Screen()
    k=Koch(random.randrange(4), random.randrange(100)+50)

    k.snowflake()
    wn.exitonclick()

main()
