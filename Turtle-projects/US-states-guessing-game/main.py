import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while all_states:
    answer_state = screen.textinput(title=f"{50-len(all_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        correct_state = data[data.state == answer_state]

        t = turtle.Turtle()
        t.penup()
        t.color("black")
        t.hideturtle()
        t.goto(correct_state.x.item(), correct_state.y.item())
        t.write(correct_state.state.item())
        all_states.remove(answer_state)


#states_to_learn.csv
states = pandas.DataFrame(all_states)
states.to_csv("states_to_learn.csv")