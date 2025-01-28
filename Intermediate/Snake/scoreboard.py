from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        # Update High Score
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Reset Score
        self.score = 0

        self.update_scoreboard()