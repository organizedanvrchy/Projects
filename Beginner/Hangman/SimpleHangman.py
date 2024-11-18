# Hangman
import os
import time
import random
from hangman_words import word_list
from hangman_art import HANGMANPICS

# Main function to execute program
def main():
    # Pick a random word from list
    chosen_word = random.choice(word_list)

    # Convert word to blanks
    blank_word = blanker(chosen_word)

    # Keep track of guessed letters
    guessed_letters = []

    # Keep track of attempts left
    attempts_remaining = 6

    print("Welcome to Hangman!")
    input("Press enter to begin!")

    while "_" in blank_word and attempts_remaining > 0:
        # Clear the terminal before displaying the next state
        clear_screen()  

        # Display hangman ASCII art
        incorrect_guesses = 6 - attempts_remaining
        print(HANGMANPICS[incorrect_guesses])

        print("-------------------------------------------------------")
        print(f"Current attempt: {blank_word}")
        print("-------------------------------------------------------")
        print(f"Attempts left: {attempts_remaining}")
        if len(guessed_letters) > 0:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print("-------------------------------------------------------")

        # Get user guessed letter
        guess = input("\nGuess a letter: ").lower()
        
        # Check for valid input
        if len(guess) != 1 or not guess.isalpha():
            print(f"\nInvalid input. Please enter a single alphabetical character.")
            time.sleep(2)
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"\nYou already guessed '{guess}'. Try again.")

        # Replace blanks with guessed letter and update blanks
        elif guess in chosen_word:
            print(f"\nCorrect! '{guess}' is in the word.")
            blank_word = blank_replacer(chosen_word, blank_word, guess)

        # Otherwise, guess was incorrect
        else:
            print(f"\nIncorrect! '{guess}' is not in the word.")
            attempts_remaining -= 1
        
        # Allow time for feedback to display
        time.sleep(2)

        # Update guessed letter set
        if guess not in guessed_letters:
            guessed_letters.append(guess)

    clear_screen()
    incorrect_guesses = 6 - attempts_remaining

    if "_" not in blank_word:
        print(HANGMANPICS[incorrect_guesses])
        print(f"\nCongratulations! You guessed the word: {chosen_word}")
    else:
        print(HANGMANPICS[-1])
        print(f"\nGame over! The word was: {chosen_word}")

# Clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Converts word to blanks
def blanker(word):
    blank_string = "_" * len(word)
    return blank_string

# Replace blanks with guessed letter
def blank_replacer(word, blank, guess):
    blanks_list = list(blank)

    for i, char in enumerate(word):
        if char == guess:
            blanks_list[i] = guess

    return ''.join(blanks_list)

# Run main
if __name__ == "__main__":
    main()
