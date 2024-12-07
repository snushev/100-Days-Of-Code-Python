from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records', index=False)
else:
    to_learn = data.to_dict(orient='records', index=False)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(upper_text, text="French", fill="black")
    canvas.itemconfig(lower_text, text=current_card["French"], fill="black")
    canvas.itemconfig(image, image=old_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(upper_text, text="English", fill="white")
    canvas.itemconfig(lower_text, text=current_card["English"], fill="white")
    canvas.itemconfig(image, image=new_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=old_image)

upper_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
lower_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()








window.mainloop()

