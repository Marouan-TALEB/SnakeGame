"""
====================================================
                    SNAKE MODULE 🐍
====================================================
Author: Marouan Taleb
Part of: Snake Game Project

Description:
    This module defines the Snake class, which controls
    the snake's creation, movement, and growth.

Class:
    Snake
        - Creates the initial snake body.
        - Handles movement, direction control, and segment addition.

Constants:
    x       : Starting coordinates for initial snake body.
    M       : Movement distance per step.
    UP, DOWN, LEFT, RIGHT : Direction constants in degrees.

Methods:
    __init__()          : Initializes the snake object.
    creatsnake()        : Creates the initial 3-segment snake.
    add_seg()           : Adds a new segment to the snake tail.
    mouveforward()      : Moves the snake forward by updating positions.
    up(), down(), 
    left(), right()     : Change the snake’s direction while preventing
                          reverse movement.

====================================================
"""

from turtle import Turtle
import time

x = [(0, 0), (-20, 0), (-40, 0)]
M = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.square_list = []
        self.creatsnake()

    def creatsnake(self):
        for i in x:
            timi = Turtle(shape="square")
            timi.color("white")
            timi.penup()
            timi.goto(i)
            self.square_list.append(timi)

    def add_seg(self):
        timi = Turtle(shape="square")
        timi.color("white")
        timi.penup()
        timi.goto(self.square_list[-1].xcor(), self.square_list[-1].ycor())
        self.square_list.append(timi)

    def mouveforward(self):
        for seg_num in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[seg_num - 1].xcor()
            new_y = self.square_list[seg_num - 1].ycor()
            self.square_list[seg_num].goto(new_x, new_y)
        self.square_list[0].forward(M)

    def up(self):
        if self.square_list[0].heading() != DOWN:
            self.square_list[0].setheading(UP)

    def down(self):
        if self.square_list[0].heading() != UP:
            self.square_list[0].setheading(DOWN)

    def left(self):
        if self.square_list[0].heading() != RIGHT:
            self.square_list[0].setheading(LEFT)

    def right(self):
        if self.square_list[0].heading() != LEFT:
            self.square_list[0].setheading(RIGHT)
