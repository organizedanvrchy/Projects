from tkinter import *
from tkinter import messagebox
import random
import json
import string

def generator():
    # Clear password field (if already populated)
    password_entry.delete(0, END)

    # Generate list of uppercase and lowercase letters
    alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_up = [x.upper() for x in alphabet_low]
    symbols = ['!', '?', "$", "#", "&"]
    letter_list = alphabet_low + alphabet_up + symbols

    # Generate of string of specified length with random selection of letters and numbers
    length = 15
    random_password = ''.join(random.choice(letter_list + [str(i) for i in range(1, 10)]) for _ in range(length))
    password_entry.insert(0, random_password)

def searcher():
    # Grab user entry and ensure it matches with stored data key format
    website = website_entry.get()
    website = string.capwords(website)
    
    try:
        # Check for existing .json
        with open("data.json", "r") as file:
            # Read existing data
            data = json.load(file)
            if website in data:
                # Grab email and password from .json file and display them
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message=f"{website} not found in data file")

    except FileNotFoundError:
        messagebox.showerror(title="Warning", message="Data file does not exist")

def save_data():
    # Get user entries for each field
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Create Dictionary to store data in .json file
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Do not leave a field empty!")

    # Otherwise, ask user for confirmation and save data 
    else:
        try:
            # Check for existing .json
            with open("data.json", "r") as file:
                # Read existing data
                data = json.load(file)          
        
        except FileNotFoundError:
            messagebox.showinfo(title="Warning", message="Data file does not exist. Creating file...")
            # Save user entries to .json file
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        
        else:
            # Update file with new data
            data.update(new_data)

            # Save updated entries to .json file
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4) 

        finally:
            # Clear all fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)   

# Main
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# First Row
website_label = Label(text="Website:", font=("Lexend", 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=16, command=searcher)
search_button.grid(column=2, row=1)

# Second Row
email_label = Label(text="Email/Username:", font=("Lexend", 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@email.com")

# Third Row
password_label = Label(text="Password:", font=("Lexend", 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate", width=16, command=generator)
gen_pass_button.grid(column=2, row=3)

# Fourth Row
add_button = Button(text="Add", width=38, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
