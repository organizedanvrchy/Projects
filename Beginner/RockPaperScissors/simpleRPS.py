import random
import os

def clear_screen():
    # Clear command based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

runner = True
while(runner):
    print("\nWelcome to the Ultimate Rock Paper Scissors Tournament\n")

    # Handle non-int inputs
    try:
        user_choice = int(input("Please choose Rock (0), Paper (1), or Scissors (2)! (Enter the number displayed next to each choice) "))
    except ValueError:
        print("\nInvalid input. Please enter a number. (0 for Rock, 1 for Paper, or 2 for Scissors)\n")
        continue

    # Play Choice
    print("You Chose: ")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        # Handle out-of-range int inputs
        print("\nInvalid choice.\nPlease enter either 0 for Rock, 1 for Paper, or 2 for Scissors\n")
        continue
    
    # Computer Choice
    print("The Computer Chose: ")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    # Outcomes
    if user_choice == computer_choice:
        print("Draw!\n")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You Win!\n")
    else:
        print("You Lose!\n")

    # Play Again
    play_again = input("Would you like to play again? (Y or N) ").upper()
    print()
    if play_again == "N":
        print("Thank you for playing! Goodbye...\n")
        runner = False
    elif play_again == "Y":
        clear_screen() # Clears terminal screen before next round
