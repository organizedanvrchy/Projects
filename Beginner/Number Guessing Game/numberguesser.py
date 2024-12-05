import random
import time

print("Welcome to the Number Guessing Game!")
print("Guess the number exactly to win!")

attempts = 0
guess = 0

def game_runner(attempts):
    print("\nI'm thinking of a number between 1 and 100...")
    target_num = random.randint(1, 100)

    attempts_remaining = attempts
    while attempts_remaining > 0:
        try:
            guess = int(input("\nMake a guess: "))
        except ValueError:
            print("\nInvalid input. Please enter a number...")
            continue
        
        attempts_remaining -= 1
        if guess < 0:
            print("\nToo far below the range I'm thinking of!")
            print(f"\nYou have {attempts_remaining} attempts remaining.")
            print("Try again...")
            continue
        elif guess > 100:
            print("\nToo far above the range I'm thinking of!")
            print(f"\nYou have {attempts_remaining} attempts remaining.")
            print("Try again...")
            continue
        elif guess < target_num and attempts_remaining >= 1:
            if abs(guess - target_num) < 10:
                print("You are close but just below the number!")
                print("Guess again...")
                print(f"\nYou have {attempts_remaining} attempts remaining.")
            else:
                print("\nToo low. Guess again...")
                print(f"\nYou have {attempts_remaining} attempts remaining.")
            continue
        elif guess > target_num and attempts_remaining >= 1:
            if abs(guess - target_num) < 10:
                print("You are close but just above the number!")
                print("Guess again...")
                print(f"\nYou have {attempts_remaining} attempts remaining.")
            else:
                print("\nToo high. Guess again...")
                print(f"\nYou have {attempts_remaining} attempts remaining.")
            continue
        elif guess == target_num:
            print("\nYou got it! Congratulations!")
            print(f"You found the number with {attempts_remaining} attempts remaining!")
            break
        else:
            break
        
    if attempts_remaining == 0 and guess != target_num:
        print(f"\nUnfortunately, the number was {target_num}.")
        print("You ran out of guesses. You Lose!")
    
def main():
    play = True
    while play:
        difficulty = input("\nChoose a difficulty. Enter 'Easy' or 'Hard': ").lower()

        if difficulty == "easy":
            game_runner(10)
        elif difficulty == "hard":
            game_runner(5)
        else:
            print("\nThat is not a difficulty. Enter either 'easy' or 'hard'...")
            continue
        
        replay = input('\nWould you like to play again? Y or N: ').upper()
        if replay == "Y":
            continue
        else:
            print("\nThank you for playing!")
            time.sleep(1)
            print("Goodbye...")
            time.sleep(2)
            play = False

if __name__ == "__main__":
    main()
