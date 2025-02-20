from tkinter import *

# Global Variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Lexend"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECK_MARKS = 0
TIMER = None

# Reset Timer Function
def reset_timer():
    global REPS

    window.after_cancel(TIMER)
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TOMATO TIMER", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    check_label.config(text="", fg=GREEN, bg=YELLOW)

# Start Timer Function
def start_timer():
    global REPS
    REPS += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        countdown(long_break_seconds)
        timer_label.config(text="LONG BREAK!", fg=RED)

    elif REPS % 2 == 0:
        countdown(short_break_seconds)
        timer_label.config(text="SHORT BREAK!", fg=PINK)
    else:
        countdown(work_seconds)
        timer_label.config(text="WORK!", fg=GREEN)

# Countdown Function
def countdown(count):
    global CHECK_MARKS
    global TIMER

    count = int(count)
    count_minute = count // 60
    count_second = count % 60
    
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            CHECK_MARKS += 1
            check_label.config(text="✓"*CHECK_MARKS, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))    

# Main
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("675x450")
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TOMATO TIMER", fg=RED, bg=YELLOW, font=(FONT_NAME, 30, "bold"), width=15)
timer_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW, width=15)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
