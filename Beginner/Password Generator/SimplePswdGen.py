#---------------------------------#
# Project #5 - Password Generator #
#---------------------------------#
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Random Password Generator")
nr_letters = int(input(f"How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

output = ""
for n in range(0, nr_letters):
    rand_letter = letters[random.randrange(0, len(letters))]
    output += rand_letter
for n in range(0, nr_numbers):
    rand_number = numbers[random.randrange(0, len(numbers))]
    output += rand_number
for n in range(0, nr_symbols):
    rand_symbol = symbols[random.randrange(0, len(symbols))]
    output += rand_symbol

output_to_list = list(output)       # Convert output to list - since strings are immutable
random.shuffle(output_to_list)      # Use shuffle to mix letters/numbers/symbols
password = ''.join(output_to_list)  # Convert back to a string after shuffling

print(f"Your password is: {password}")
