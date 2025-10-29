"""
====================================================
                    SNAKE GAME 🐍
====================================================
Author: Marouan Taleb
Description:
    This project is a simple Snake Game built using 
    Python's Turtle graphics module.

Files:
    - main.py       : Runs the game loop.
    - snake.py      : Contains the Snake class that handles movement and growth.
    - food.py       : Contains the Food class that manages random food placement.
    - score.py      : Contains the Score class that tracks and displays the score.

Controls:
    ↑  : Move Up
    ↓  : Move Down
    ←  : Move Left
    →  : Move Right

How to Play:
    Run this file (main.py). The snake moves continuously.
    Eat the food to grow longer and increase your score.
    Avoid colliding with the walls or yourself.

Requirements:
    - Python 3.x
    - turtle module (comes with Python standard library)

====================================================
"""

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake.creatsnake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x = 1
game_on = True
while game_on:
    screen.update() 
    time.sleep(0.1)
    snake.mouveforward()

    if snake.square_list[0].distance(food) < 20:
        food.move()
        score.clear()
        score.add_score(x)
        snake.add_seg()
        x += 1

    if (
        snake.square_list[0].xcor() > 280 
        or snake.square_list[0].xcor() < -280 
        or snake.square_list[0].ycor() > 280 
        or snake.square_list[0].ycor() < -280
    ):
        game_on = False
        score.game_over()

    for i in snake.square_list[1:]:
        if snake.square_list[0].distance(i) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
