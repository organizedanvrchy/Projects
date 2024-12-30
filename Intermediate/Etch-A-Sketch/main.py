import turtle as t

# Objects
timmy = t.Turtle()
screen = t.Screen()

# Functions
def move_up():
    timmy.setheading(90)
    timmy.forward(10)

def move_left():
    timmy.setheading(180)
    timmy.forward(10)

def move_down():
    timmy.setheading(270)
    timmy.forward(10)

def move_right():
    timmy.setheading(360)
    timmy.forward(10)

def clear_screen():
    timmy.penup()
    timmy.home()
    screen.reset()

# Main
def main():
    screen.screensize(canvwidth=500, canvheight=500, bg=None)
    screen.listen()
    screen.onkey(key="w", fun=move_up)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="s", fun=move_down)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key="c", fun=clear_screen)
    screen.exitonclick()

if __name__ == "__main__":
    main()
