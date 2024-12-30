import turtle as t
import random

def main():
    # Screen Setup
    screen = t.Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Place your bet!", prompt="Which of these colored turtles will win the race? (Red/Orange/Blue/Green/Purple): ").lower()

    # Turtle Setup
    colors = ["red", "orange", "green", "blue", "purple"]
    y_positions = [-80, -40, 0, 40, 80]
    all_turtles = []

    for turtle_index in range(0, 5):
        turtle = t.Turtle(shape="turtle")
        turtle.color(colors[turtle_index])
        turtle.penup()
        turtle.goto(x=-235, y=y_positions[turtle_index])
        all_turtles.append(turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                win_message = f"You Won! The {winning_color} turtle is the winner!\n"
                lose_message = f"You Lost! The {winning_color} turtle is the winner!\n"

                if winning_color == user_bet:
                    turtle.home()
                    res = screen.textinput(title="The race is over!", prompt=(win_message + "Press Cancel to exit."))
                else:
                    turtle.home()
                    res = screen.textinput(title="The race is over!", prompt=(lose_message + "Press Cancel to exit."))

                if res is None:
                    screen.clear()
                    screen.bye()

    screen.exitonclick()

if __name__ == "__main__":
    main()
