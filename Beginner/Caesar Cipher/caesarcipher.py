import time
import ccart

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    print(ccart.logo)
    while(1):
        direction = input("Type 'encode' to encrypt | Type 'decode' to decrypt: ").lower()
        text = input("Enter your message: ").lower()
        shift = int(input("Type the shift number: "))

        cipher(direction, text, shift)

        choice = input("Would you like to continue? Y or N: ").lower()
        if choice == "y":
            continue
        else:
            print("Goodbye..")
            time.sleep(2)
            break

def cipher(direction, text, shift):
    output_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            original_index = alphabet.index(letter)
            shifted_index = (original_index + shift) % len(alphabet)
            output_text += alphabet[shifted_index]
        else:
            output_text += letter
    
    print(f"Here is your {direction}d message: {output_text}\n")

# Run main
if __name__ == "__main__":
    main()
