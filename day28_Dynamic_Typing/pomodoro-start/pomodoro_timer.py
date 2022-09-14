from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ---------------------------- #

def reset_timer():
    window.after_cancel(timer)  # cancels timer we set up in countdown mechanism
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------ #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # if it's the 8th break
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # if it's the 2nd, 4th or 6th rep
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)  # if it's the 1st, 3rd, 5th, 7th rep
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM -------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # keeps largest whole number ex) 4.8 is 4
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,
                             count - 1)  # .after() executes a command after a time delay in milliseconds
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")  # reads image file in particular location of computer
canvas.create_image(100, 112, image=tomato_image)  # cut width & height by half to center image on screen (fine tune)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Checkmark label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()