import turtle as t
import pandas as pd

# Create Turtle to Show State Name on Map
def create_turtle(states_data, answer_state_formatted):
    turt = t.Turtle()
    turt.hideturtle()
    turt.penup()

    answer_row_data = states_data[states_data.state == answer_state_formatted]
    turt.goto(answer_row_data.x.item(), answer_row_data.y.item())
    turt.write(answer_row_data.state.item())

# Main
def main():
    # Screen
    screen = t.Screen()
    screen.title("U.S. States Game")

    # Image Object and Screen Adjustment
    image = "blank_states_img.gif"
    screen.addshape(image)
    t.shape(image)

    # States Data
    states_data = pd.read_csv("50_states.csv")
    states_list = states_data.state.tolist()

    # Counter
    max_states = len(states_data == "state")
    guessed_states = []
    state_counter = 0

    while state_counter < max_states:
        # User Input
        answer_state = screen.textinput(title=f"{state_counter}/50 Attempts | Guess the State", prompt="What's the name of a State?")
        answer_state_formatted = answer_state.title()

        # Exit
        if answer_state_formatted == "Exit":
            missed_states = []
            for state in states_list:
                if state not in guessed_states:
                    missed_states.append(state)

            game_results = pd.DataFrame(missed_states)
            game_results.to_csv("states_missed.csv")

            break

        # Check User Input Against Data
        if answer_state_formatted in states_list:
            guessed_states.append(answer_state_formatted)
            state_counter += 1 # Allows for duplicate guesses to count towards attempts
            create_turtle(states_data, answer_state_formatted)
        else:
            state_counter += 1 # Allows for wrong answers to increase attempts

if __name__ == "__main__":
    main()
