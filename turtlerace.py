from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the ace? Enter the colour: ")
print(user_bet)

colours = ["red", "yellow", "orange", "green", "blue", "purple"]
all_turtles = []

y_position = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position + 30)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner_colour = turtle.pencolor()

            if winner_colour == user_bet:
                print(f"Congrats you've won! The {winner_colour} turtle won the race! :)")
            else:
                print(f"Sorry you've lost! The {winner_colour} turtle won the race! :(")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
