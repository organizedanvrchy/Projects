import turtle as tl
from snake import Snake
from snack import Snack
from scoreboard import Scoreboard
import time

# Screen Setup
screen = tl.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Snake Object
snake = Snake()

# Snack Object
snack = Snack()

# Scoreboard
scoreboard = Scoreboard()

# Key Bindings
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

# Main
def main():
    game_is_on = True

    while game_is_on:
        # Update screen
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with snacks
        if snake.head.distance(snack) < 15:
            snack.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with walls
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()
        
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()
