from tkinter import *

def calculate():
    uinput = usr_input.get()
    formatted_uinput = int(uinput)
    kilometers = formatted_uinput * 1.609344
    formatted_kilometers = round(kilometers, 3)
    label3.config(text=f"{formatted_kilometers}")

# Create Window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

# Entry
usr_input = Entry(width=10)
usr_input.grid(column=1, row=1)

# Label 1
label1 = Label(text="Miles")
label1.grid(column=2, row=1)

# Label 2
label2 = Label(text="=")
label2.grid(column=0, row=2)

# Label 3
label3 = Label(text="0")
label3.grid(column=1, row=2)

# Label 4
label4 = Label(text="Km")
label4.grid(column=2, row=2)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()
