import random
from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
colors = ["red", "blue", "green", "yellow", "black", "gray", "orange"]


def turtle_game(num_side):
    angle = 360 / num_side
    for x in range(num_side):
        timmy_the_turtle.speed(1)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for sides in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    turtle_game(sides)

# second method -----------------------------
# for num_side in range(3, 11):
#     angle = 360 / num_side
#     for x in range(num_side):
#         timmy_the_turtle.speed(1)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# first method--------------------------------
# for x in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# for move in range(2):
#     timmy_the_turtle.speed(1)
#     for a in range(1):
#         timmy_the_turtle.color("green")
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(120)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(120)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(120)
#         for b in range(1):
#             timmy_the_turtle.color("red")
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(90)
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(90)
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(90)
#             timmy_the_turtle.forward(100)
#             timmy_the_turtle.right(90)
#             for c in range(1):
#                 timmy_the_turtle.color("blue")
#                 timmy_the_turtle.forward(100)
#                 timmy_the_turtle.right(72)
#                 timmy_the_turtle.forward(100)
#                 timmy_the_turtle.right(72)
#                 timmy_the_turtle.forward(100)
#                 timmy_the_turtle.right(72)
#                 timmy_the_turtle.forward(100)
#                 timmy_the_turtle.right(72)
#                 timmy_the_turtle.forward(100)
#                 timmy_the_turtle.right(72)
#                 for d in range(1):
#                     timmy_the_turtle.color("yellow")
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     timmy_the_turtle.forward(100)
#                     timmy_the_turtle.right(60)
#                     for e in range(1):
#                         timmy_the_turtle.color("gray")
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)
#                         timmy_the_turtle.forward(100)
#                         timmy_the_turtle.right(45)




screen = Screen()
screen.exitonclick()
