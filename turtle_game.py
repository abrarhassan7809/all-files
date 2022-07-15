import random
import turtle
from turtle import Turtle, Screen

tim1 = Turtle()
tim2 = Turtle()
# tim3 = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=1000, height=500)


user_bet = screen.textinput(title="make your bet", prompt="which turtle win the race : ")
colors = ["red", "blue", "green", "yellow", "purple", "black"]
y_position = [-100, -40, 20, 80, 140, 200]
all_trutles = []

for turtle_index in range(0, 6):
    tim1 = Turtle(shape="turtle")
    tim1.penup()
    tim1.color(colors[turtle_index])
    tim1.speed(1)
    tim1.goto(x=-440, y=y_position[turtle_index])
    all_trutles.append(tim1)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_trutles:
        if turtle.xcor() > 440:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                winning_turtle = screen.textinput(title="winning turtle", prompt=f"you win the race '{winning_color}'")
            else:
                winning_turtle = screen.textinput(title="winning turtle", prompt=f"you loss the race ! winner is : '{winning_color}'")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

# # -------------1---------------
# tim1.shape("turtle")
# tim1.color("red")
# tim1.speed(1)
# tim1.penup()
# tim1.goto(x=-230, y=-50)
#
# # ------------2------------------
# tim2.shape("turtle")
# tim2.color("green")
# tim2.speed(1)
# tim2.penup()
# tim2.goto(x=-230, y=0)
#
# # ------------3------------------
# tim3.shape("turtle")
# tim3.color("purple")
# tim3.speed(1)
# tim3.penup()
# tim3.goto(x=-230, y=50)


# first game-----------------------------

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def clear_fun():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="c", fun=clear_fun)

