"""
====================================================
                    FOOD MODULE 🍎
====================================================
Author: Marouan Taleb
Part of: Snake Game Project

Description:
    This module defines the Food class, which represents
    the food object in the Snake Game. The food appears at
    random positions on the screen and is eaten by the snake
    to increase its size and score.

Class:
    Food(Turtle)
        - Inherits from the Turtle class.
        - Handles creation and random repositioning of food.

Methods:
    __init__()  : Initializes the food with shape, color, and size.
    move()      : Moves the food to a random location within the game window.

====================================================
"""

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
