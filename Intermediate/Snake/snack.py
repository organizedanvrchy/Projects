from turtle import Turtle
import random

# Snack Class
class Snack(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Range
        start = -280
        end = 280
        step = 20

        # Position snack in random location
        ran_x = random.choice(range(start, end + 1, step))
        ran_y = random.choice(range(start, end + 1, step))
        self.goto(ran_x, ran_y)