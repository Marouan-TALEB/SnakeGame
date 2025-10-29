"""
====================================================
                    SCORE MODULE 🎯
====================================================
Author: Marouan Taleb
Part of: Snake Game Project

Description:
    This module defines the Score class, which manages 
    the player's score display and game-over message.

Class:
    Score(Turtle)
        - Inherits from the Turtle class.
        - Displays the score at the top of the screen.
        - Handles game-over text when the player loses.

Methods:
    __init__()      : Initializes the score display.
    add_score(x)    : Updates and displays the current score.
    game_over()     : Displays the 'Game Over' message in the center.

====================================================
"""

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__(visible=0)
        self.penup()
        self.color("cyan")
        self.goto(0, 310)
        self.add_score(0)

    def add_score(self, x):
        self.write(f"Score = {x}", False, align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 16, "normal"))
