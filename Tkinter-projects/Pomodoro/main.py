from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_text.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break)
        title_text.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 1:
        countdown(work_sec)
        title_text.config(text="Work", fg=GREEN, bg=YELLOW)
    else:
        countdown(short_break)
        title_text.config(text="Break", fg=PINK, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):


    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        winsound.Beep(440, 1000)
        start_timer()
        check = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            check += "✔"
            checkmark.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



title_text = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_text.grid(column=1, row=0)
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
