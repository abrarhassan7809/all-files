import turtle
import pandas

screen = turtle.Screen()
screen.title("states game")
screen.setup(width=500, height=500)
data = pandas.read_csv("states_name.txt")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 7:
    ans_state = screen.textinput(title=f"{len(guess_state)}/50 states", prompt="another name").title()

    if ans_state == "Exit":
        break
    if ans_state in all_states:
        guess_state.append(ans_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == ans_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(ans_state)
