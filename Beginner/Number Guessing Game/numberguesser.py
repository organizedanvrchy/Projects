import random
import time

print("Welcome to the Number Guessing Game!")
print("Guess the number exactly to win!")

attempts = 0
play = True

while play:
    print("\nI'm thinking of a number between 1 and 100...")
    target_num = random.randint(1, 100)
    print(target_num)
    difficulty = input("\nChoose a difficulty. Enter 'Easy' or 'Hard': ").lower()

    if difficulty == "easy":
        attempts = 10
        guess = 0

        while attempts > 0:
            try:
                guess = int(input("\nMake a guess: "))
            except ValueError:
                print("Invalid input. Please enter a number...")
                continue
            
            attempts -= 1
            if guess < 0:
                print("Too far below the range I'm thinking of!")
                print("Try again...")
                continue
            elif guess > 100:
                print("Too far above the range I'm thinking of!")
                print("Try again...")
                continue
            elif guess < target_num:
                if attempts >= 1:
                    print("\nToo Low.\nGuess again...")
                    print(f"\nYou have {attempts} attempts remaining.")
                continue
            elif guess > target_num:
                if attempts >= 1:
                    print("\nToo high. Guess again...")
                    print(f"\nYou have {attempts} attempts remaining.")
                continue
            elif guess == target_num:
                print("\nYou got it! Congratulations!")
                print(f"You found the number with {attempts} attempts remaining!")
                break
            else:
                print("Invalid Entry.")
                break
            
        if attempts == 0 and guess != target_num:
            print(f"\nUnfortunately, the number was {target_num}.")
            print("You ran out of guesses. You Lose!")

    elif difficulty == "hard":
        attempts = 5
        guess = 0
        
        while attempts > 0:
            try:
                guess = int(input("\nMake a guess: "))
            except ValueError:
                print("Invalid input. Please enter a number...")
                continue

            attempts -= 1
            if guess < 0:
                print("Too far below the range I'm thinking of!")
                print("Try again...")
                continue
            elif guess > 100:
                print("Too far above the range I'm thinking of!")
                print("Try again...")
                continue
            elif guess < target_num:
                if attempts >= 1:
                    print("\nToo Low.\nGuess again...")
                    print(f"\nYou have {attempts} attempts remaining.")
                continue
            elif guess > target_num:
                if attempts >= 1:
                    print("\nToo high. Guess again...")
                    print(f"\nYou have {attempts} attempts remaining.")
                continue
            elif guess == target_num:
                print("\nYou got it! Congratulations!")
                print(f"You found the number with {attempts} attempts remaining!")
                break
            else:
                print("Invalid Entry.")
                break

        if attempts == 0 and guess != target_num:
            print(f"\nUnfortunately, the number was {target_num}.")
            print("You ran out of guesses. You Lose!")

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
